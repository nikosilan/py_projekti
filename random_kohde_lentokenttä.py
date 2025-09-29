flight_count = 0
continents_sql_list = ["EU"] # Alussa on vain Eurooppa, sitten tähän lisätään muita

def hae_avatut_maanosat(flight_count):
    # Määritellään maanosia, jotka avautuvat lentojen määrän mukaan
    maanosat_jarjestys = ["EU", "NA", "SA", "AS", "OC", "AF", "AN"]  # Europe, North America, South America, etc.
    # Palauttaa listan maanosista, jotka ovat tähän mennessä avautuneet
    avattujen_maara = min((flight_count // 5) + 1, len(maanosat_jarjestys))
    return maanosat_jarjestys[:avattujen_maara]

# valitsee sattumanvaraisesti 3 isoa lentokenttää ja PALAUTTAA listan
def random_kohteet(yhteys):
    destinations = []

    for kohde in range(3):
        sql = (f'SELECT airport.name, country.name '
               f'FROM airport '
               f'INNER JOIN country ON airport.iso_country = country.iso_country '
               f'WHERE country.continent IN ("{continents_sql_list}")'
               f'AND TYPE like "large_airport" ORDER BY RAND() LIMIT 1;')

        '''sql = "SELECT name FROM airport WHERE type LIKE 'large_airport' ORDER BY RAND() LIMIT 1;"'''
        # vanha pyyntö tietokannasta

        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchone()

        # purkaa tuplen ja lisää kenttien nimet listaan destinations
        if tulos:
            lentokentan_nimi = tulos[0]
            maan_nimi = tulos[1]
            destinations.append((lentokentan_nimi, maan_nimi))

    return destinations  # palautetaan lista


# tulostaa listan nätisti numeroituna
def tulosta_numeroitu_lista(lista):
    for indeksi, (alkio, maanimi) in enumerate(lista, start=1):
        print(f"{indeksi}. {alkio} in {maanimi}")
    return

avatut_maanosat = hae_avatut_maanosat(flight_count)
continents_sql_list.append(avatut_maanosat)

# pääohjelma
# kohteet = random_kohteet()      # otetaan vastaan palautettu lista
# tulosta_numeroitu_lista(kohteet)
