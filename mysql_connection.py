import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='Juuso',
    password='salasana',
    autocommit=True
)

def pelaaja_haku():
    sql = f"Select screen_name From game WHERE screen_name = 'heini'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    if tulos:
        print("toimii")
    return print(tulos)

pelaaja_haku()
kayttaja = input("Anna pelajaan nimi: ")
pelaaja_haku(kayttaja)'''