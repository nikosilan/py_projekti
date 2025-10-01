from aircraft_game import peli
import mysql.connector

yhteys = mysql.connector.connect(
                host='127.0.0.1',
                port=3306,
                database='flight_game',
                user='niko',
                password='salasana',
                autocommit=True
            )






valittu_kohde = peli(yhteys)




