from log_in import kirjautuminen
from random_kohde_lentokenttä import random_kohteet
from random_kohde_lentokenttä import tulosta_numeroitu_lista


from noppa import noppa_peli

from tieto_kilpailu import tietokilpailu_peli

from hahmon_nimen_luonti import nimea_hahmo
from lataus import palkki



#yhdistäminen tietokantaan
yhteys = kirjautuminen()

#lataus palkki
#palkki()

#hahmon nimen luonti

if yhteys:
    hahmon_nimi = input("Nimeä hahmo (pelkkä etunimi/käyttäjänimi): ").strip()
    tulos = nimea_hahmo(yhteys, hahmon_nimi)

    if tulos == 1:
        print(f"Hahmosi nimi on: {hahmon_nimi}")
    else:
        print("Nimen päivitys ei onnistunut.")

        
while True:
        
        # valitsee sattumanvaraisesti 3 isoa lentokenttää ja PALAUTTAA listan
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



