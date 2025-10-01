import random

airport = "Lontoo"  # lentokenttä

def airport_service_event():
    """
    Satunnainen tapahtuma lentokentällä:
    - Huolto
    - Tankkaus
    - Ei tapahtumaa
    """
    service_chance = 0.4   # 40% huolto
    refuel_chance  = 0.4   # 40% tankkaus

    roll = random.random()
    if roll < service_chance:
        return "Huolto: Lentokoneesi on tarkastettu ja korjattu."
    elif roll < service_chance + refuel_chance:
        return "Tankkaus: Lentokoneesi on tankattu."
    else:
        return "Ei tapahtumaa."
#funktion suoritus

tapahtuma = airport_service_event()
print(f"Saavuit lentokentälle: {airport}")
print(f"Tapahtuma: {tapahtuma}")
