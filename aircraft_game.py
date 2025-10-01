from geopy.distance import geodesic
from aircraft_config import aircraft, aircraft_fuel_burn, FUEL_DENSITY, CO2_EMISSION_FACTOR
from aircraft_utils import get_airport_info, get_current_fuel, update_fuel, random_kohteet
from aircraft_lista import tulosta_numeroitu_lista

def peli(yhteys):
    current_airport = get_airport_info("EFHK", yhteys)
    if not current_airport:
        print("Error: EFHK not found in database!")
        return

    total_distance = 0
    flights = 0
    total_emissions = 0

    print(f"🌍 Welcome! Starting at {current_airport[1]} ({current_airport[0]}) in {current_airport[2]}.")
    print(f"Your aircraft: {aircraft}\n")

    while True:
        kohteet = random_kohteet(yhteys)
        tulosta_numeroitu_lista(kohteet)

        choice = input("\nChoose destination (1-3) or q to quit: ")
        if choice.lower() == "q":
            print(f"\nGame over! Flights: {flights}, Total distance: {total_distance:.1f} km")
            print(f"Total CO₂ emissions: {total_emissions:.1f} kg")
            break

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
                    break

                if fuel_needed > current_fuel:
                    print("Not enough fuel for this flight!")
                    continue

                update_fuel(yhteys, -fuel_needed)

                print(f"\n Flight {flights+1}:")
                print(f"Etäisyys {current_airport[1]} ja {name} airportin välillä on {distance:.1f} km")
                print(f"   Käytetty polttoaine: {fuel_needed:.1f} litraa ({aircraft})")

                fuel_needed_kg = fuel_needed * FUEL_DENSITY
                co2_emissions = fuel_needed_kg * CO2_EMISSION_FACTOR
                print(f"   Arvioidut CO₂-päästöt: {co2_emissions:.1f} kg")

                total_distance += distance
                total_emissions += co2_emissions
                flights += 1
                current_airport = valittu
            else:
                print("Choose 1, 2, or 3.")
        except ValueError:
            print("Enter a number (1-3) or q to quit.")
