import mysql.connector

yhteys = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='flight_game',
            user='niko',
            password='salasana',
            autocommit=True
        )

<<<<<<< HEAD
# valitsee sattumanvaraisesti 3 isoa lentokenttää ja PALAUTTAA listan
=======
# lista, johon random_kohteet-funktio sijoittaa lentokenttien nimet
destinations = []

# valitsee sattumanvaraisesti 3 isoa lentokenttää
>>>>>>> 7fae2c234588b61cb9e6a0e6d10b655a492805db
def random_kohteet():
    destinations = []   

    for kohde in range(3):
<<<<<<< HEAD
        sql = "SELECT name FROM airport WHERE type LIKE 'large_airport' ORDER BY RAND() LIMIT 1;"
=======
        sql = (f"SELECT name FROM airport WHERE TYPE like 'large_airport' ORDER BY RAND() LIMIT 1;")
>>>>>>> 7fae2c234588b61cb9e6a0e6d10b655a492805db
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
kohteet = random_kohteet()      # otetaan vastaan palautettu lista
tulosta_numeroitu_lista(kohteet)
