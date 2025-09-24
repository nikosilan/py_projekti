import random

airport = "Lontoo"  # lentokenttä
TREASURES = ["€10 seteli", "€20 seteli", "koru", "matkamuisto"]

def airport_event():
    treasure_chance = 0.15  # 15% mahdollisuus löytää aarre
    robbed_chance = 0.10    # 10% mahdollisuus tulla ryöstetyksi

    roll = random.random()
    if roll < treasure_chance:
        item = random.choice(TREASURES)
        return f"Löysit aarteen: {item}!"
    elif roll < treasure_chance + robbed_chance:
        return "Ryöstö! Menetit jotain arvokasta."
    else:
        return "Ei tapahtumaa."

#funktion suoritus
tapahtuma = airport_event()

print(f"Saavuit lentokentälle: {airport}")
print(f"Tapahtuma: {tapahtuma}")
