# noppa_peli
import random
import time
#from log_in import kirjautuminen
#yhteys = kirjautuminen()


def get_raha(yhteys, hahmo_id=1):
    cursor = yhteys.cursor()

    sql = "SELECT raha FROM game WHERE id = %s"
    cursor.execute(sql, (hahmo_id,))
    result = cursor.fetchone()
    cursor.close()
    pisteet = result[0]

    return pisteet

def noppa_peli(pisteet):
    tietokone_noppa1 = random.randint(1, 6)
    tietokone_noppa2 = random.randint(1, 6)

    print(f"Tietokone heitti: {tietokone_noppa1} ja {tietokone_noppa2}")
    time.sleep(1.5)

    while True:
        syote = input("Haluatko heittää noppia? (y/n): ").lower()

        if syote == "y":
            pelaaja_noppa1 = random.randint(1, 6)
            pelaaja_noppa2 = random.randint(1, 6)

            print(f"Sinun heittosi: {pelaaja_noppa1} ja {pelaaja_noppa2}")

            if ((pelaaja_noppa1, pelaaja_noppa2) == (tietokone_noppa1, tietokone_noppa2)
                    or (pelaaja_noppa2, pelaaja_noppa1) == (tietokone_noppa1, tietokone_noppa2)):
                palkinto = random.randint(1, 100)
                print(f"Onnittelut! Heitot täsmäsivät, saat {palkinto}€!")
                return palkinto
            else:
                print("Heitot eivät täsmänneet, ei rahaa.")

        elif syote == "n":
            print("Et halunnut heittää noppia, peli päättyi.")
            return pisteet
        else:
            print("Väärä syöte, anna 'y' tai 'n'.")

def update_raha(yhteys, pisteet, hahmo_id=1):
    cursor = yhteys.cursor()

    sql = "UPDATE game SET raha = raha + %s WHERE id = %s"
    cursor.execute(sql, (pisteet, hahmo_id))
    yhteys.commit()
    cursor.close()


#   Pääohjelmaan alkuun
# from noppa2 import get_raha, noppa_peli, update_raha

#   Pääohjelmaan kun halutaan ajaa noppa_pelin
# pisteet = get_raha(yhteys)
# pisteet = noppa_peli(pisteet)
# update_raha(pisteet, yhteys)
# print(f"Sinulla on nyt {pisteet}€.")