import mysql.connector


yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='Daniel',
    password='DA10',
    autocommit=True
)

def pelaaja_haku_bensa(bensa_muutos):
    MAX_BENSA = 240000  # Max fuel
    MIN_BENSA = 0        # Min fuel

    kursori = yhteys.cursor()

    # Get current fuel from database
    kursori.execute("SELECT bensa FROM game WHERE id = 1")
    tulos = kursori.fetchone()

    if tulos is not None:
        nykyinen_bensa = tulos[0]
        uusi_bensa = nykyinen_bensa + bensa_muutos

        # Clamp the fuel between MIN and MAX
        if uusi_bensa > MAX_BENSA:
            uusi_bensa = MAX_BENSA
        elif uusi_bensa < MIN_BENSA:
            uusi_bensa = MIN_BENSA

        # Update the database
        sql = "UPDATE game SET bensa = %s WHERE id = 1"
        kursori.execute(sql, (uusi_bensa,))
        yhteys.commit()

        print(f"Fuel updated to: {uusi_bensa} liters")
    else:
        print("Player not found.")
bensa_muutos = float(input("How much fuel to add/remove: "))
pelaaja_haku_bensa(bensa_muutos)