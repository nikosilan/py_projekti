# noppa.py
import random

def noppa_peli(pisteet):
    syote = input("Haluatko heittää noppia nyt? (Y/n): ")

    random_num = int(random.randint(1, 6))
    tietokoneen_vastaava_silmäluku = (random_num, random_num)

    if syote.lower() == "y":
        p_noppa_1, p_noppa_2 = (random_num, random_num)
        tulos_t = f'Tietokone heitti {tietokoneen_vastaava_silmäluku[0]} ja {tietokoneen_vastaava_silmäluku[1]}'
        tulos_p = f'Heitetty {p_noppa_1} ja {p_noppa_2}'

        print(tulos_t)
        print(tulos_p)

        if tietokoneen_vastaava_silmäluku == (p_noppa_1, p_noppa_2):
            palkinto = int(random.randint(1,100))
            print(f"Olet voittanut timantin, sinulle myönnetään {palkinto}")
            pisteet += palkinto
    elif syote.lower() == "n":
        print("Et halua heitä noppia, olet poistunut tehtävästä.")
    else:
        print("Väärin komento, yritä uudelleen.")

    return pisteet  # Palautetaan päivitetyt pisteet

def main():
    pisteet = 0
    pisteet += noppa_peli(pisteet)
    print(f"Lopulliset pisteet: {pisteet}")

if __name__ == "__main__":
    main()
