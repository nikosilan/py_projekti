#tietokilpailu peli
import random

pisteet = 0

def tietokilpailu_peli(pisteet):
    tietopankki = {
        "Kuinka monta maanosaa maailmassa on?": "7",
        "Mikä on maailman suurin valtameri?": "Tyynimeri",
        "Mikä on veden kemiallinen kaava?": "H2O",
        "Mikä on Suomen pääkaupunki?": "Helsinki",
        "Mikä planeetta tunnetaan punaisena planeettana?": "Mars",
        "Kuka maalasi Mona Lisan?": "Leonardo da Vinci",
        "Mikä on maailman korkein vuori?": "Mount Everest",
        "Mikä on maailman nopein maaeläin?": "Gepardi",
        "Mikä kieli on eniten puhuttu maailmassa?": "Mandariinikiina",
        "Minkä komediaryhmän mukaan Python-ohjelma on nimetty?" : "Monty Python",
        "Mikä eläin pyton on?": "käärme",
        "Kumpi on tilastollisesti turvallisempi matkustamisen muoto, lentäminen vai autolla ajaminen?": "lentäminen",
        "Millä sanalla Pythonissa aloitetaan ehtolause?": "if",
        "Missä kaupungissa sijaitsee Eiffel-torni?": "ranska",
        "Minkä maan pääkaupunki on Oslo?": "norja"
    }

    kysymykset = list(tietopankki.items())
    
    # Valitaan 3 satunnaista kysymystä
    satunnaiset_kysymykset = random.sample(kysymykset, 3)

    for kysymys, oikea_vastaus in satunnaiset_kysymykset:
        print(kysymys)
        pelaajan_vastaus = input("Anna vastaus: ").strip()
        if pelaajan_vastaus.lower() == oikea_vastaus.lower():
            random_piste_maara = random.randint(1, 10)
            print(f"Onnea! Vastasit oikein ja ansaitset {random_piste_maara} pistettä.")
            pisteet += random_piste_maara
        else:
            print("Valitettavasti et päässyt läpi ja et ansainnut senttiäkään!")
            break

    print(f"\nPelin lopussa sinulla on yhteensä {pisteet} pistettä.")
    return pisteet

# Pääohjelmaan
# tietokilpailu_peli(pisteet)