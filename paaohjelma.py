from log_in import kirjautuminen
from random_kohde_lentokenttä import random_kohteet
from random_kohde_lentokenttä import tulosta_numeroitu_lista


#yhdistäminen tietokantaan
yhteys = kirjautuminen()

# valitsee sattumanvaraisesti 3 isoa lentokenttää ja PALAUTTAA listan
kohteet = random_kohteet(yhteys)

# tulostaa listan nätisti numeroituna
tulosta_numeroitu_lista(kohteet)