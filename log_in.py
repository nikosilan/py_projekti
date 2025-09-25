import mysql.connector

def kirjautuminen():
    global user, salasana
    nimi = input("Käyttäjä: ")

    yhteys = None

    try:
        # Tarkistetaan käyttäjänimi ja luodaan oikea yhteys
        if nimi.lower() == "niko":
            yhteys = mysql.connector.connect(
                host='127.0.0.1',
                port=3306,
                database='flight_game',
                user='niko',
                password='salasana',
                autocommit=True
            )
            user = "niko"
            salasana = "salasana"


        elif nimi.lower() == "juuso":
            yhteys = mysql.connector.connect(
                host='127.0.0.1',
                port=3306,
                database='flight_game',
                user='Juuso',
                password='salasana',
                autocommit=True
            )

        elif nimi.lower() == "daniel":
            yhteys = mysql.connector.connect(
                host='127.0.0.1',
                port=3306,
                database='flight_game',
                user='Daniel',
                password='DA10',
                autocommit=True
            )

        elif nimi.lower() == "illia":
            yhteys = mysql.connector.connect(
                host='127.0.0.1',
                port=3306,
                database='flight_game',
                user='illia',
                password='salasana3',
                autocommit=True
            )

        else:
            print("Tuntematon käyttäjä.")


        # onko yhteys onnistunut
        if yhteys and yhteys.is_connected():
            print(f"Yhteys käyttäjällä {nimi} onnistui!")

    except mysql.connector.Error as err:
        print(f"Yhteys epäonnistui: {err}")

    return yhteys


# kirjautuminen()