import random
import time

def aircraft_huolto(yhteys):
    """Arpoo satunnaisen lentokonehuollon ja tulostaa, mikä huolto tehtiin."""

    # Todennäköisyys, että huolto tapahtuu (esim. 30 %)
    huolto_mahdollisuus = 0.8

    if random.random() > huolto_mahdollisuus:
        print("🛠️ Lentokone on hyvässä kunnossa — ei huoltoa tällä kertaa!\n")
        return

    # Lista mahdollisista huolloista (nimi, todennäköisyys)
    huollot = [
        ("✈️ Moottorin tarkastus", 0.5),
        ("🔧 Öljynvaihto", 0.5),
        ("🛞 Renkaiden tarkistus", 0.5),
        ("💨 Polttoainejärjestelmän puhdistus", 0.5),
        ("⚙️ Hydraulijärjestelmän huolto", 0.5),
        ("🧰 Täydellinen huolto", 0.5)
    ]

    # Arvotaan huolto todennäköisyyksien mukaan
    r = random.random()
    cumulative = 0.0
    for nimi, todennakoisyys in huollot:
        cumulative += todennakoisyys
        if r <= cumulative:
            print(f"🔩 Huolto tehtiin: {nimi}\n")
            time.sleep(2)
            return

    # Jos mikään huolto ei osu
    print("🛠️ Ei huoltoa tällä kertaa.\n")
