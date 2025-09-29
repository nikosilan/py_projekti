
import random

def tietokilpailu_peli(pisteet):
    tietopankki = {
        "Kuinka monta maanosaa maailmassa on?": "7",
        "Mikä on maailman suurin valtameri?": "Tyynimeri",
        "Mikä on veden kemiallinen kaava?": "H2O",
        "Minkä komediaryhmän mukaan Python-ohjelma on nimetty?" : "Monty Python",
        "Mikä eläin pyton on?": "käärme",
        "Kumpi on tilastollisesti turvallisempi matkustamisen muoto, lentäminen vai autolla ajaminen?": "lentäminen",
        "Millä sanalla Pythonissa aloitetaan ehtolause?": "if",
        "Missä kaupungissa sijaitsee Eiffel-torni?": "ranska",
        "Minkä maan pääkaupunki on Oslo?": "norja"
    }

    kysymykset = list(tietopankki.items())
    
    # Valitaan 3 satunnaista kysymystä
    satunnaiset_kysymykset = random.sample(kysymykset, k=min(3, len(kysymykset)))

    for kysymys, oikea_vastaus in satunnaiset_kysymykset:
        print(kysymys)
        pelaajan_vastaus = input("Anna vastaus: ").strip()
        if pelaajan_vastaus.lower() == oikea_vastaus.lower():
            random_piste_määrä = random.randint(1, 10)
            print(f"Onnea! Vastasit oikein ja ansaitset {random_piste_määrä} pistettä.")
            pisteet += random_piste_määrä
        else:
            print("Valitettavasti et päässyt läpi ja et ansainnut senttiäkään!")
            break

    print(f"\nPelin lopussa sinulla on yhteensä {pisteet} pistettä.")
    return pisteet


