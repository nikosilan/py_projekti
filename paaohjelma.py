from log_in import kirjautuminen
from random_kohde_lentokenttä import random_kohteet
from random_kohde_lentokenttä import hae_avatut_maanosat
from random_kohde_lentokenttä import tulosta_numeroitu_lista

from noppa import noppa_peli
from tieto_kilpailu import tietokilpailu_peli

from lataus import palkki

from rahamuutos import raha_saldo
from rahamuutos import raha_muutos

from hahmon_luonti import nimea_hahmo

# Kaikki muuttujat tähän
#yhdistäminen tietokantaan
yhteys = kirjautuminen()
flight_count = 0 # Lennot määrä, käytetään sitten maanosien aukeamisessa
continents_sql_list = [] # Alussa on vain Eurooppa, sitten tähän lisätään muita

#lataus palkki
#palkki()

#hahmon nimen luonti
''' 
Hei, tehdäänkö meidän alkupiste Suomesta? (Helsinki-Vantaa lentokenttä)
'''


#   Tämä voi laittaa pääohjelmaan
# pelin alkun jälkeen
nimi = input("Syötä oma nimi: ")
nimea_hahmo(yhteys, nimi)
'''
# Tää mietin laittamaan vielä edelliseen funktioon keskiviikkona
print("Avatut maanosat:", ", ".join(continents_sql_list))
'''

'''      
while True:

    # Tää pitäis tarkistaa koko ajan lennot määrät toimiakseen
    # mut voidaan tehdä tarkistus jos esim 
    # if flight_count == (5, 10, 15, 20, 25, 30) or flight_count >= 30
    # tai tarkistus ennen lentoa, joka ei vaatis sitten if-ehtoa ollenkaa
    # mielestäni while True toimis oikein hyvinkin 
    
    avatut_maanosat = hae_avatut_maanosat(flight_count)
    continents_sql_list.extend(avatut_maanosat)
    
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

    
        # Illian vielä on tarkistettava molempia pelejä myös saada näitä pisteitä suoraan rahaksi 
        # Tai lisätä muuttujaa pisteeseen ja sitten kun peli on tehty,
        # vaihtaa pisteet rahaksi ja päivittää sitä tietokantaan

        #noppapeli
        #pisteet = 10  # aloitetaan esimerkiksi 10 pisteestä
        #pisteet = noppa_peli(pisteet)
        #print(f"Uudet pisteet: {pisteet}")


        #tietokilpailu
        #pisteet = 0
        #pisteet = tietokilpailu_peli(pisteet)
        #print(f"Uudet pisteet pääohjelmassa: {pisteet}")



        #arvo kolme kenttää
        #tulosta_numeroitu_lista(kohteet)'
'''


