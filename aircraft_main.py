from log_in import kirjautuminen
import sys
import time
from aircraft_config import aircraft, aircraft_fuel_burn, FUEL_DENSITY, CO2_EMISSION_FACTOR
from aircraft_utils import get_airport_info, get_current_fuel, update_fuel, random_destination
from aircraft_lista import tulosta_numeroitu_lista, search_for_open_destinations

#from noppa import noppa_peli
from tieto_kilpailu import tietokilpailu_peli

from lataus import palkki

from rahamuutos import raha_saldo
from rahamuutos import raha_muutos

from hahmon_luonti import nimea_hahmo

#from lentokone_data import peli

from aircraft_game import peli

from noppa2 import get_raha, noppa_peli, update_raha

yhteys = kirjautuminen()

flight_count = 0
current_airport = get_airport_info("EFHK", yhteys)
if not current_airport:
    print("Error: EFHK not found in database!")

def menu():
    choice = input(
        "Welcome to Aircraft game! This is the menu of this game."
        "\nPlease choose the option to proceed:"
        "\n1. Start game"
        "\n2. Player stats"
        "\n3. Exit game"
        "\n> "
    )
    return choice

def stats(yhteys):
    sql = "SELECT screen_name, bensa, raha FROM game WHERE id = 1;"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()

    if result:
        name, bensa, raha = result
        print(f"📊 Your stats:\nYour player {name} has earned {raha}€ money, "
              f"has {bensa} liters of fuel left, and has flown {flight_count} times.")
    else:
        print("⚠️ No player data found.")

def main():
    global flight_count, current_airport
    try:
        while True:  # Main menu loop
            choice = menu()

            if choice == "1":
                print("Starting game...")
                flight_count, current_airport = peli(yhteys, flight_count, current_airport)

            elif choice == "2":
                stats(yhteys)
                while True:
                    confirm = input("Do you want to go back to the menu? (y/n): \n> ")
                    if confirm.lower() == "y":
                        print("Returning you back to the menu...\n")
                        break
                    elif confirm.lower() == "n":
                        print("Ok, updating your stats...\n")
                        stats(yhteys)
                    else:
                        print("Type in correct answer.")

            elif choice == "3":
                confirm = input("Are you sure you want to quit this game? (y/n): \n> ")
                if confirm.lower() == "y":
                    print("See you next time!")
                    sys.exit(0)
                elif confirm.lower() == "n":
                    print("Returning you back to the menu...\n")
                    continue
                else:
                    print("Type in correct answer.")

            else:
                print("Invalid choice, please select 1, 2, or 3.\n")

    except KeyboardInterrupt:
        print("\nGame interrupted. Exiting safely.")
        sys.exit(0)


if __name__ == "__main__":
    main()