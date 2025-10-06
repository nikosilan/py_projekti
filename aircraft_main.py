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

# from lentokone_data import peli

from aircraft_game import peli

from noppa2 import get_raha, noppa_peli, update_raha

yhteys = kirjautuminen()
palkki()

current_airport = get_airport_info("EFHK", yhteys)
if not current_airport:
    print("Error: EFHK not found in database!")

def menu():
    #tulostaa päävalikon ja palauttaa käyttäjän valinnan
    choice = input(
        "Welcome to Aircraft game! This is the menu of this game."
        "\nPlease choose the option to proceed:"
        "\n1. Start game"
        "\n2. Create new player"
        "\n3. Player stats"
        "\n4. Exit game"
        "\n> "
    )
    return choice

def stats(yhteys):
    #tulostaa tilastot
    sql = "SELECT screen_name, bensa, raha, flights FROM game WHERE id = 1;"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()

    if result:
        name, bensa, raha, flight_count= result
        print(f"📊 Your stats:\nYour player {name} has earned {raha}€ money, "
              f"has {bensa} liters of fuel left, and has flown {flight_count} times.")
    else:
        print("⚠️ No player data found.")

def main():
    #valikko rakenne
    global current_airport
    try:
        while True:
            choice = menu()

            if choice == "1":
                print("Starting game...")
                peli(yhteys)


            elif choice == "2":
                while True:
                    confirm_choice = input(
                        "You are about to make a new player. Your default changes will be wiped if you"
                        "\ndecide to overwrite the existing player. Are you sure? (y/n)"
                        "\n> ")
                    if confirm_choice.lower() == "y":
                        nimi = input("Your new name (max 20): ")
                        nimea_hahmo(yhteys, nimi, hahmo_id=1)
                        break  # exit loop after creating new player
                    elif confirm_choice.lower() == "n":
                        print("Returning you back to the main menu.")
                        time.sleep(2)
                        break
                    else:
                        print("Type in correct answer.")
                        time.sleep(1)
            elif choice == "3":
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

            elif choice == "4":
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