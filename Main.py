import mysql.connector

# Kysytään käyttäjänimi
nimi = input("Käyttäjä: ")

# Tarkistetaan käyttäjänimi ja luodaan oikea yhteys
if nimi == "niko":
    yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='niko',
        password='salasana',
        autocommit=True
    )

elif nimi == "Juuso":
    yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='Juuso',
        password='salasana',
        autocommit=True
    )