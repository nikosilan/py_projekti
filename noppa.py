# noppa_peli
import random
import mysql.connector

yhteys = mysql.connector.connect(
                host='127.0.0.1',
                port=3306,
                database='flight_game',
                user='Juuso',
                password='salasana',
                autocommit=True
            )


def noppa_peli(pisteet):
    tietokone_noppa1 = random.randint(1, 1)
    tietokone_noppa2 = random.randint(1, 1)

    print(f"Tietokone heitti: {tietokone_noppa1} ja {tietokone_noppa2}")

    while True:
        syote = input("Haluatko heittää noppia? (y/n): ").lower()

        if syote == "y":
            pelaaja_noppa1 = random.randint(1, 1)
            pelaaja_noppa2 = random.randint(1, 1)

            print(f"Sinun heittosi: {pelaaja_noppa1} ja {pelaaja_noppa2}")

            if (pelaaja_noppa1, pelaaja_noppa2) == (tietokone_noppa1, tietokone_noppa2):
                palkinto = random.randint(1, 1000)

                sql = "UPDATE game SET raha = raha + %s WHERE id = %s;"
                kursori = yhteys.cursor()
                kursori.execute(sql, (palkinto, 1))
                yhteys.commit()

                print(f"Onnittelut! Heitot täsmäsivät, saat {palkinto}€!")
                pisteet += palkinto

                return pisteet
            else:
                print("Heitot eivät täsmänneet, ei rahaa.")

        elif syote == "n":
            print("Et halunnut heittää noppia, peli päättyi.")
            return pisteet
        else:
            print("Väärä syöte, anna 'y' tai 'n'.")


def main():
    pisteet = 0
    pisteet = noppa_peli(pisteet)
    print(f"Lopullinen saldo: {pisteet}")


if __name__ == "__main__":
    main()
