from log_in import kirjautuminen
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

# Kaikki muuttujat tähän
#yhdistäminen tietokantaan
# yhteys = kirjautuminen()
# flight_count = 0 # Lennot määrä, käytetään sitten maanosien aukeamisessa
'''
def menu():
    return print("Welcome to Aircraft game! This is the menu of this game."
          "Please choose the option to proceed:"
          "1. Start game"
          "2. Player stats"
          "3. Exit game")'''
#lataus palkki
# palkki()
'''
#hahmon nimen luonti
nimi = input("Syötä oma nimi: ")
nimea_hahmo(yhteys, nimi)

while True:



    peli(yhteys)

    #tietokilpailu
    pisteet = get_raha(yhteys)
    pisteet = tietokilpailu_peli(pisteet)
    update_raha(pisteet,yhteys)
    print(f"Sinulla on nyt {pisteet}€.")

    #noppapeli
    pisteet = get_raha(yhteys)
    pisteet = noppa_peli(pisteet)
    update_raha(pisteet, yhteys)
    print(f"Sinulla on nyt {pisteet}€.")

Hei, tehdäänkö meidän alkupiste Suomesta? (Helsinki-Vantaa lentokenttä)
'''

'''
    
        #rahamäärä
        #raha_määrä = int(input("syötä rahan määrä: "))
        #raha_muutos(raha_määrä)
        raha_saldo()

    # Tää laitetaan pienen story-alkun jälkeen
    kohteet = random_kohteet(yhteys)
    tulosta_numeroitu_lista(kohteet)
       
        kysymys = input("Valitse kohde kirjoittamalla numero 1, 2 tai 3: ")
        # muunnetaan syöte kokonaisluvuksi 
        try:
            valinta = int(kysymys) - 1  
            if valinta in [0, 1, 2]:
                sana = kohteet[valinta]   # tallennetaan valittu kohde
                print("Valitsit kohteen:", sana)
               
                
            else:
                print("Virheellinen numero (valitse 1, 2 tai 3).")
        except ValueError:
            print("Syötteen täytyy olla numero.")
'''


