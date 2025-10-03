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

def main():
    choice = menu()

    if choice == "1":
        print("Starting game...")
        peli(yhteys, flight_count)

    elif choice == "2":
        print("Stats are being developed now.")

    elif choice == "3":
        while True:
            confirm = input("Are you sure you want to quit this game? (y/n): "
                            "\n> ")
            if confirm.lower() == "y":
                print("See you next time!")
                sys.exit(0)
            elif confirm.lower() == "n":
                print("Returning you back to the menu...")
                menu()
            else:
                print("Type in correct answer.")
                break

    else:
        print("Invalid choice, please select 1, 2, or 3.")

if __name__ == "__main__":
    main()