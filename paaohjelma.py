from log_in import kirjautuminen
from random_kohde_lentokenttä import random_kohteet
from random_kohde_lentokenttä import tulosta_numeroitu_lista


from noppa import noppa_peli

from tieto_kilpailu import tietokilpailu_peli


from lataus import palkki

from rahamuutos import raha_saldo
from rahamuutos import raha_muutos

from hahmon_luonti import nimea_hahmo

#yhdistäminen tietokantaan
yhteys = kirjautuminen()

#lataus palkki
#palkki()

#hahmon nimen luonti

#   Tämä voi laittaa pääohjelmaan
nimi = input("Syötä oma nimi: ")
nimea_hahmo(yhteys, nimi)



      
while True:
        #rahamäärä
        #raha_määrä = int(input("syötä rahan määrä: "))
        #raha_muutos(raha_määrä)
        raha_saldo()


        
        #valitsee sattumanvaraisesti 3 isoa lentokenttää ja PALAUTTAA listan
        kohteet = random_kohteet(yhteys)


        # tulostaa listan nätisti numeroituna

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



