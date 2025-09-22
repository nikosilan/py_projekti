import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='Juuso',
    password='salasana',
    autocommit=True
)

def pelaaja_haku(pelaaja):
    sql = f"select screen_name From game WHERE screen_name = {pelaaja}"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()

    return print(tulos)


käyttäjä = input("Anna pelajaan nimi: ").lower
pelaaja_haku(käyttäjä)

