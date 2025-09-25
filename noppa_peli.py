import random

pisteet = 0 # oletetaan pisteet-muuttujan olevan palkkana

def noppa_peli(pisteet):
    syöte = input("Haluatko heittää noppia nyt? (Y/n): ")

    random_num = int(random.randint(1, 6))
    tietokoneen_vastaava_silmäluku = []

    t_noppa_1, t_noppa_2 = (random_num, random_num)
    tulos_t = f'Tietokone heitti {t_noppa_1} ja {t_noppa_2}'

    if syöte.lower() == "y":
        p_noppa_1, p_noppa_2 = (random_num, random_num)
        tulos_p = f'Heitetty {p_noppa_1} ja {p_noppa_2}'

        print(tulos_t)
        print(tulos_p)

        if tietokoneen_vastaava_silmäluku == (p_noppa_1, p_noppa_2):
            palkinto = int(random.randint(1,100))
            print(f"Olet voittanut tietokoneen, sinulle myönnetään {palkinto}")
            pisteet += palkinto
    elif syöte.lower() == "n":
        tulos = "Et halua heitä noppia, olet poistunut tehtävästä."
        print(tulos)
    else:
        print("Väärin komento, yritä uudelleen.")
    return pisteet

def main():
    noppa_peli(pisteet)

if __name__ == "__main__":
    main()