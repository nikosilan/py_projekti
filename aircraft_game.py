import sys
import os
import time
from geopy.distance import geodesic
from aircraft_config import aircraft, aircraft_fuel_burn, FUEL_DENSITY, CO2_EMISSION_FACTOR
from aircraft_utils import get_airport_info, get_current_fuel, update_fuel, random_destination, get_flight_count, update_flight_count, get_current_airport, update_current_airport
from aircraft_lista import tulosta_numeroitu_lista, search_for_open_destinations

from lataus import palkki

from noppa2 import get_raha, update_raha, noppa_peli
from tieto_kilpailu import tietokilpailu_peli

from aarteet2 import airport_event

from rahamuutos import raha_saldo, raha_muutos

# from log_in import kirjautuminen
# yhteys = kirjautuminen()


def peli(yhteys):
    total_distance = 0
    total_emissions = 0

    flight_count = get_flight_count(yhteys, hahmo_id=1)

    current_airport = get_current_airport(yhteys)
    if not current_airport:
        print("⚠️ Current airport not set. Defaulting to EFHK.")
        current_airport = ("EFHK", "Helsinki Airport", "Finland")

    # Lentojen hinta
    if flight_count == 0:
        flight_cost = 70
    elif 1 <= flight_count <= 4:
        flight_cost = 150
    elif 5 <= flight_count < 10:
        flight_cost = 200
    elif 10 <= flight_count < 15:
        flight_cost = 300
    elif 15 <= flight_count < 20:
        flight_cost = 500
    elif 20 <= flight_count < 25:
        flight_cost = 600
    elif 25 <= flight_count < 30:
        flight_cost = 900
    elif flight_count >= 30:
        flight_cost = 1000

    while True:
        print(f"\n🌍 Welcome! Starting at {current_airport[1]} ({current_airport[0]}) in {current_airport[2]}.")
        print(f"Your aircraft: {aircraft}\n")
        print(f"The price of the flight is: {flight_cost}€\n")

        kohteet = random_destination(yhteys, flight_count)
        tulosta_numeroitu_lista(kohteet)

        choice = input("\nChoose destination (1-3) or q to quit: ")
        if choice.lower() == "q":
            print(f"\n✈️ Game over! Flights: {flight_count}, Total distance: {total_distance:.1f} km")
            print(f"Total CO₂ emissions: {total_emissions:.1f} kg")
            print("Returning you back to main menu... \n")
            time.sleep(2)
            return

        try:
            choice = int(choice)
            if 1 <= choice <= 3:
                valittu = kohteet[choice - 1]
                icao, name, country, lat, lon = valittu

                coords_current = (current_airport[3], current_airport[4])
                coords_dest = (lat, lon)
                distance = geodesic(coords_current, coords_dest).kilometers

                fuel_needed = (distance / 100) * aircraft_fuel_burn
                current_fuel = get_current_fuel(yhteys)
                if current_fuel is None:
                    print("Player fuel not found in DB.")
                    return

                while fuel_needed > current_fuel:
                    print("❌ Not enough fuel for this flight!\n")
                    while True:
                        fuel_choice = input(
                            "Do you want to tank the aircraft now?\n"
                            "1. Yes, I would like to tank (100€)\n"
                            "2. No, I don't have enough money. I want to earn money first.\n"
                            "3. No, I don't want to tank this time.\n"
                            "> "
                        )

                        if fuel_choice == "1":
                            raha = raha_saldo(yhteys)
                            if raha >= 100:
                                palkki()
                                update_fuel(yhteys, 240000)
                                update_raha(yhteys, pisteet=-100)  # refill fuel
                                print("✅ Refueled! Ready for flight.\n")
                                current_fuel = get_current_fuel(yhteys)
                                break
                            else:
                                print("You don't have enough money to refuel your aircraft. You need to earn money first.\n")
                                break

                        elif fuel_choice == "2":
                            print(" ")
                            while True:
                                game_choice = input(
                                    "Okay! You have some mini-games that you can choose from:"
                                    "\n1. Noppa peli"
                                    "\n2. Tietokilpailu"
                                    "\n> "
                                )

                                if game_choice == "1":
                                    pisteet = raha_saldo(yhteys)
                                    pisteet = noppa_peli(pisteet)
                                    raha_muutos(yhteys, pisteet)
                                    print(f"You now have {pisteet}€ to spend.")
                                    time.sleep(2)
                                    break

                                elif game_choice == "2":
                                    pisteet = raha_saldo(yhteys)
                                    pisteet = tietokilpailu_peli(pisteet)
                                    raha_muutos(yhteys, pisteet)
                                    print(f"You now have {pisteet}€ to spend.")
                                    time.sleep(2)
                                    break

                                else:
                                    print("❌ Invalid option, please try again.\n")
                        elif fuel_choice == "3":
                            print("Flight canceled due to insufficient fuel. Flight canceled.")
                            return
                        else:
                            print("❌ Invalid option, please try again.\n")

                update_fuel(yhteys, -fuel_needed)

                print(f"\n🛫 Flight {flight_count + 1}:")
                print(f"From {current_airport[1]} to {name} airport = {distance:.1f} km")
                print(f"Fuel used: {fuel_needed:.1f} liters ({aircraft})")

                fuel_needed_kg = fuel_needed * FUEL_DENSITY
                co2_emissions = fuel_needed_kg * CO2_EMISSION_FACTOR
                print(f"Estimated CO₂ emissions: {co2_emissions:.1f} kg")

                total_distance += distance
                total_emissions += co2_emissions
                flight_count += 1
                update_flight_count(yhteys, flight_count)

                print(f"💸 Flight cost: {flight_cost}€")
                update_raha(yhteys, -flight_cost)

                current_airport = valittu
                update_current_airport(yhteys, valittu[0])
                print(f"📍 You are now at {current_airport[1]} ({current_airport[0]}) in {current_airport[2]}.")
            else:
                print("❌ Choose 1, 2, or 3.")
        except ValueError:
            print("❌ Enter a number (1-3) or q to quit.")

        airport_event(yhteys)
        time.sleep(2)
        print("\n")
        while True:  # continue-choice loop
            continue_choice = input(
                "You have now free time to spend."
                "\nHow would you like to spend your time now?"
                "\n1. I would like to take some tasks to earn more money."
                "\n2. I would like to fly more (make sure you have enough money)."
                "\n3. Exit to main menu"
                "\n> "
            )

            if continue_choice == "1":
                while True:  # mini-game selection loop
                    game_choice = input(
                        "Okay! You have some games that you can choose from:"
                        "\n1. Noppa peli"
                        "\n2. Tietokilpailu"
                        "\n> "
                    )

                    if game_choice == "1":
                        pisteet = raha_saldo(yhteys)
                        pisteet = noppa_peli(pisteet)
                        raha_muutos(yhteys, pisteet)
                        print(f"You now have {pisteet}€ to spend.")
                        time.sleep(2)
                        break  # exit mini-game loop, back to continue_choice menu

                    elif game_choice == "2":
                        pisteet = raha_saldo(yhteys)
                        pisteet = tietokilpailu_peli(pisteet)
                        raha_muutos(yhteys, pisteet)
                        print(f"You now have {pisteet}€ to spend.")
                        time.sleep(2)
                        break  # exit mini-game loop, back to continue_choice menu

                    else:
                        print("❌ Invalid option, please try again.")

            elif continue_choice == "2":
                print("\nLoading another pack of flights available just for you!")
                time.sleep(2)
                return peli(yhteys)

            elif continue_choice == "3":
                print("Returning to main menu...")
                time.sleep(2)
                return

            else:
                print("❌ Invalid option, please try again.")