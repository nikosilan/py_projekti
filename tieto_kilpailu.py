import random
import math

# Oletetaan, että se on rahatili, haasteiden toteuttaessa saadaan palkan
pisteet = 0

# Funktio, joka ajaa pelin
def tietokilpailu_peli(pisteet):
    tietopankki = {"Kuinka monta maanosaa maailmassa on?": "7",
                   "Mikä on maailman suurin valtameri?": "Tyynimeri",
                   "Mikä on veden kemiallinen kaava?": "H2O"}

    kysymykset = list(tietopankki.items())

    for _ in range(1):
        for index in range(len(kysymykset)):
            for kysymys, oikea_vastaus in kysymykset:
                print(kysymys)
                pelaajan_vastaus = input("Anna vastaus: ").strip()
                if pelaajan_vastaus.lower() == oikea_vastaus.lower():
                    random_piste_määrä = random.randint(1, 10)
                    print(f"Onnea! Vastasit oikein ja ansaitset {random_piste_määrä} pistettä.")
                    pisteet += random_piste_määrä
                else:
                    print("Valitettavasti et päässyt läpi ja et ansainnut senttiäkään!")
                    break
            else:
                break
        else:
            break

    print(f"\nPelin lopussa sinulla on yhteensä {pisteet} pistettä.")

    return pisteet # saatu palkka

tietokilpailu_peli(pisteet)
# korjata 3 satunnaista määrää kysymystä, se toistuu enemmän