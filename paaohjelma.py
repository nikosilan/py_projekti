from log_in import kirjautuminen
from random_kohde_lentokenttä import random_kohteet
from random_kohde_lentokenttä import tulosta_numeroitu_lista

from noppa import noppa_peli

from tieto_kilpailu import tietokilpailu_peli

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


#tietokilpailu
pisteet = 0
pisteet = tietokilpailu_peli(pisteet)
print(f"Uudet pisteet pääohjelmassa: {pisteet}")
