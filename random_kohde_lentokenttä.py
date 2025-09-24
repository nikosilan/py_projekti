import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='Juuso',
    password='salasana',
    autocommit=True
)

# lista, johon random_kohteet-funktio sijoittaa lentokenttien nimet
destinations = []

# valitsee sattumanvaraisesti 3 lentokenttää
def random_kohteet():

    for kohde in range(3):
        sql = (f"SELECT name FROM airport"
               f"WhERE TYPE like 'large_airport' ORDER BY RAND() LIMIT 1;")
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchone()

        #purkaa tuplen ja lisää kenttien nimet listaan destinations
        lentokentan_nimi = tulos[0]
        destinations.append(lentokentan_nimi)

    return

# tulostaa listan nätisti numeroituna
def tulosta_numeroitu_lista(lista):
    for indeksi, alkio in enumerate(lista, start=1):
        print(f"{indeksi}. {alkio}")
    return

random_kohteet()
tulosta_numeroitu_lista(destinations)



