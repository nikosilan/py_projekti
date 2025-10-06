#tietokilpailu peli
import random
# from log_in import kirjautuminen
# yhteys = kirjautuminen()


def get_raha(yhteys, hahmo_id=1):
    cursor = yhteys.cursor()

    sql = "SELECT raha FROM game WHERE id = %s"
    cursor.execute(sql, (hahmo_id,))
    result = cursor.fetchone()
    cursor.close()
    pisteet = result[0]

    return pisteet

def tietokilpailu_peli(pisteet):
    saatu_pisteet = 0 # se on väliaikainen asia, joka sitten näyttää pelin lopussa saatu pisteet
    # 1 piste = 1 euro
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
            random_piste_maara = random.randint(1, 100)
            print(f"Onnea! Vastasit oikein ja ansaitset {random_piste_maara}€.")
            pisteet += random_piste_maara
            saatu_pisteet += random_piste_maara
        else:
            print("Valitettavasti et päässyt läpi ja et ansainnut senttiäkään!")
            break

    print(f"\nPelin lopussa sinulla on yhteensä {saatu_pisteet}€.")
    return saatu_pisteet

def update_raha(yhteys, pisteet, hahmo_id=1):
    cursor = yhteys.cursor()

    sql = "UPDATE game SET raha = raha + %s WHERE id = %s"
    cursor.execute(sql, (pisteet, hahmo_id))
    yhteys.commit()
    cursor.close()


#   Pääohjelmaan alkuun
# from tieto_kilpailu import get_raha, tietokilpailu_peli, update_raha

#   Pääohjelmaan kun halutaan ajaa tietokilpailun peli
# pisteet = get_raha(yhteys)
# pisteet = tietokilpailu_peli(pisteet)
# update_raha(yhteys, pisteet)
# print(f"Sinulla on nyt {pisteet}€.")