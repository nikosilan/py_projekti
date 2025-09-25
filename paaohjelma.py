from log_in import kirjautuminen
from random_kohde_lentokenttä import random_kohteet
from random_kohde_lentokenttä import tulosta_numeroitu_lista

from noppa import noppa_peli

# peli_kayttaja.py
from noppa import noppa_peli

#yhdistäminen tietokantaan
yhteys = kirjautuminen()

# valitsee sattumanvaraisesti 3 isoa lentokenttää ja PALAUTTAA listan
kohteet = random_kohteet(yhteys)

# tulostaa listan nätisti numeroituna
tulosta_numeroitu_lista(kohteet)


#noppapeli
pisteet = 10  # aloitetaan esimerkiksi 10 pisteestä
pisteet = noppa_peli(pisteet)
print(f"Uudet pisteet: {pisteet}")
