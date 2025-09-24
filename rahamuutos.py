import mysql.connector


yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='Daniel',
    password='DA10',
    autocommit=True
)

def raha_haku(pelaaja):
    sql = f"SELECT raha FROM game WHERE screen_name = '{pelaaja}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()

    return print(tulos)

pelaaja = input("Syötä pelaajan nimi: ").strip()
raha_haku(pelaaja)

