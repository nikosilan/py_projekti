import random
import time
from geopy.distance import geodesic
from aircraft_config import aircraft, aircraft_fuel_burn, FUEL_DENSITY, CO2_EMISSION_FACTOR
from aircraft_utils import GameState, Airport, Minigames, Events, session


class FlightGame:
    def __init__(self, yhteys):
        self.conn = yhteys
        self.current_airport = Airport.get_current_airport(self.conn) or ("EFHK", "Helsinki Airport", "Finland", 60.32, 24.96)
        self.flight_count = GameState.get_flight_count(self.conn)
        self.total_distance = 0
        self.total_emissions = 0
        self.state = "menu"   # default
        self.choices = []
        self.temp_data = {}   # store temporary info like selected destination

    def get_flight_cost(self):
        fc = self.flight_count
        if fc == 0: return 70
        elif 1 <= fc <= 4: return 150
        elif 5 <= fc < 10: return 200
        elif 10 <= fc < 15: return 300
        elif 15 <= fc < 20: return 500
        elif 20 <= fc < 25: return 600
        elif 25 <= fc < 30: return 900
        else: return 1000

    def step(self, user_input):
        out = []
        self.choices.clear()

        if self.state == "menu":
            out.append("Welcome! Choose an option:\n1. Start game\n2. Player stats\n3. Exit")
            self.choices = ["1", "2", "3"]
            self.state = "menu_wait"
            return out, self.choices

        elif self.state == "menu_wait":
            if user_input == "1":
                self.state = "choose_destination"
                return self.step(None)
            elif user_input == "2":
                sql = """SELECT screen_name, bensa, raha, flights FROM game WHERE id = 1;"""
                cursor = self.conn.cursor()
                cursor.execute(sql)
                result = cursor.fetchone()
                cursor.close()
                if result:
                    name, bensa, raha, flights = result
                    out.append(f"Stats: {name}, Fuel: {bensa}, Money: {raha}€, Flights: {flights}")
                    self.choices = ["Return"]
                    if user_input == "Return":
                        self.state = "menu"
                else:
                    out.append("No player data found.")
                self.state = "menu"
                return out, self.choices
            elif user_input == "3":
                out.append("Goodbye!")
                self.state = "exit"
                return out, []
            else:
                out.append("Invalid choice, pick 1-3")
                return out, self.choices

        elif self.state == "choose_destination":
            # Show flight info
            flight_cost = self.get_flight_cost()
            raha = GameState.raha_saldo(self.conn)
            avatut_maanosat = GameState.search_for_open_destinations(self.flight_count)
            out.append(f"Starting at {self.current_airport[1]} ({self.current_airport[0]})")
            out.append(f"Your aircraft: {aircraft}")
            out.append(f"Flight cost: {flight_cost}€, you have {raha}€")
            out.append(f"Opened destinations: {', '.join(avatut_maanosat)}")

            # Generate destinations
            kohteet = GameState.random_destination(self.conn, self.flight_count)
            self.temp_data["destinations"] = kohteet
            for idx, (_, name, country, _, _) in enumerate(kohteet, 1):
                out.append(f"{idx}. {name} ({country})")
            out.append("Choose destination 1-3 or q to quit")
            self.choices = ["1", "2", "3", "q"]
            self.state = "destination_wait"
            return out, self.choices

        elif self.state == "destination_wait":
            # Prevent crashing on None
            if user_input is None:
                return out, self.choices

            # Handle NEXT from refuel and sooner minigames
            if user_input == "Next":
                self.state = "choose_destination"
                return self.step(None)

            if user_input.lower() == "q":
                out.append(f"Game over! Total flights: {self.flight_count}, Distance: {self.total_distance:.1f} km, CO2: {self.total_emissions:.1f} kg")
                self.state = "menu"
                return out, []
            try:
                choice_idx = int(user_input) - 1
                valittu = self.temp_data["destinations"][choice_idx]
                icao, name, country, lat, lon = valittu
                self.temp_data["selected_destination"] = valittu
            except (ValueError, IndexError):
                out.append("Invalid choice, pick 1-3")
                return out, self.choices

            # Check money
            flight_cost = self.get_flight_cost()
            raha = GameState.raha_saldo(self.conn)
            if raha < flight_cost:
                out.append(f"Not enough money ({raha}€) to pay {flight_cost}€")
                self.state = "menu"
                return out, []

            # Check fuel
            coords_current = (self.current_airport[3], self.current_airport[4])
            coords_dest = (lat, lon)
            distance = geodesic(coords_current, coords_dest).kilometers
            fuel_needed = (distance / 100) * aircraft_fuel_burn
            current_fuel = Airport.get_current_fuel(self.conn)
            if fuel_needed > current_fuel:
                self.temp_data["fuel_needed"] = fuel_needed
                self.state = "refuel"
                out.append(f"Not enough fuel ({current_fuel:.1f}L) for flight requiring {fuel_needed:.1f}L"
                           f"\nDo you wish to refuel for 100€ or earn money by sidetasks?")
                self.choices = ["Tank", "Earn", "Quit"]
                return out, self.choices

            # Execute flight
            Airport.get_current_fuel(self.conn)
            Airport.update_fuel(self.conn, -fuel_needed)
            fuel_needed_kg = fuel_needed * FUEL_DENSITY
            co2_emissions = fuel_needed_kg * CO2_EMISSION_FACTOR
            self.total_distance += distance
            self.total_emissions += co2_emissions
            self.flight_count += 1
            GameState.update_flight_count(self.conn, self.flight_count)
            GameState.raha_muutos(self.conn, -flight_cost)
            self.current_airport = valittu
            Airport.update_current_airport(self.conn, icao)
            Events.aircraft_huolto(self.conn)
            Events.airport_event(self.conn)

            out.append(f"Flight done: {self.current_airport[1]} ({icao})")
            out.append(f"Distance: {distance:.1f} km, Fuel used: {fuel_needed:.1f} L, CO2: {co2_emissions:.1f} kg")
            self.state = "choose_destination"
            return out, ["Next"]

        # Refuel
        elif self.state == "refuel":
            if user_input is None:
                return out, self.choices
            elif user_input == "Tank":
                current_fuel = Airport.get_current_fuel(self.conn)
                fuel_to_add = 240000 - current_fuel
                if fuel_to_add > 0:
                    Airport.update_fuel(self.conn, fuel_to_add)
                GameState.raha_muutos(self.conn, -100)
                out.append(f"✅ You have successfully refueled! You now have 240000L")
                self.choices = ["Next"]
                self.state = "destination_wait"
                return out, self.choices
            elif user_input == "Earn" or user_input == "Quit":
                self.state = "menu"
                return out, []
            return None

        else:
            out.append("Game state error")
            self.state = "menu"
            return out, []