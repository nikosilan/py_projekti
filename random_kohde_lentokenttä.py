# valitsee sattumanvaraisesti 3 isoa lentokenttää ja PALAUTTAA listan
def random_kohteet(yhteys):
    destinations = []   

    for kohde in range(3):
        sql = "SELECT name FROM airport WHERE type LIKE 'large_airport' ORDER BY RAND() LIMIT 1;"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchone()

        # purkaa tuplen ja lisää kenttien nimet listaan destinations
        lentokentan_nimi = tulos[0]
        destinations.append(lentokentan_nimi)

    return destinations  # palautetaan lista


# tulostaa listan nätisti numeroituna
def tulosta_numeroitu_lista(lista):
    for indeksi, alkio in enumerate(lista, start=1):
        print(f"{indeksi}. {alkio}")
    return


# pääohjelma
# kohteet = random_kohteet()      # otetaan vastaan palautettu lista
# tulosta_numeroitu_lista(kohteet)
