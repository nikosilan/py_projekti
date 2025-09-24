import mysql.connector


yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='Daniel',
    password='DA10',
    autocommit=True
)

def pelaaja_haku_bensa(pelaaja):
    sql = f"SELECT bensa FROM game WHERE screen_name = '{pelaaja}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()

    return print(tulos)


pelaaja_nimi = input("Enter player's screen name: ").strip()
pelaaja_haku_bensa(pelaaja_nimi)
