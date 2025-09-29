''' Käyttäkää näitä jos haluatte saada yhteyden tietokantaan '''
# from log_in import kirjautuminen
# yhteys = kirjautuminen()

flight_count = 0 # Lennot määrä, käytetään sitten maanosien aukeamisessa
continents_sql_list = [] # Alussa on vain Eurooppa, sitten tähän lisätään muita

def hae_avatut_maanosat(flight_count):
    # Määritellään maanosia, jotka avautuvat lentojen määrän mukaan
    maanosat_jarjestys = ["EU", "NA", "SA", "AS", "OC", "AF", "AN"]  # Europe, North America, South America, etc.
    # Palauttaa listan maanosista, jotka ovat tähän mennessä avautuneet
    avattujen_maara = min((flight_count // 5) + 1, len(maanosat_jarjestys))
    return maanosat_jarjestys[:avattujen_maara]

# Valitsee sattumanvaraisesti 3 isoa lentokenttää ja PALAUTTAA listan
def random_kohteet(yhteys):
    destinations = []

    # Muodostaa oikea merkkijono SQL:ään
    continents_str = ','.join(f"'{c}'" for c in continents_sql_list)

    for kohde in range(3):
        sql = (f'SELECT airport.name, country.name '
               f'FROM airport '
               f'INNER JOIN country ON airport.iso_country = country.iso_country '
               f'WHERE country.continent IN ({continents_str})'
               f'AND TYPE like "large_airport" ORDER BY RAND() LIMIT 1;')

        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchone()

        # Purkaa monikon ja lisää kenttien ja maiden nimet listaan destinations
        if tulos:
            lentokentan_nimi = tulos[0]
            maan_nimi = tulos[1]
            destinations.append((lentokentan_nimi, maan_nimi))

    return destinations  # Palautetaan lista


# Tulostaa listan nätisti numeroituna
def tulosta_numeroitu_lista(lista):
    for indeksi, (alkio, maanimi) in enumerate(lista, start=1):
        print(f"{indeksi}. {alkio} in {maanimi}")
    return

# Pääohjelma
# Avatut maanosat pitää tarkistaa koko ajan?
'''
avatut_maanosat = hae_avatut_maanosat(flight_count)
continents_sql_list.extend(avatut_maanosat)

print("Avatut maanosat:", ", ".join(continents_sql_list))

kohteet = random_kohteet(yhteys)      # otetaan vastaan palautettu lista
tulosta_numeroitu_lista(kohteet)
'''
