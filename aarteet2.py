import random
# from log_in import kirjautuminen

# yhteys = kirjautuminen()

airport = "Lontoo"  # lentokenttä
TREASURES = {"€10 seteli": 10,
             "€20 seteli": 20,
             "koru": 50,
             "matkamuisto": 200}

treasures_avaimet = ["€10 seteli", "€20 seteli", "koru", "matkamuisto"]
random.shuffle(treasures_avaimet)
satunnainen_avain = treasures_avaimet[0]

def airport_event(yhteys):
    treasure_chance = 0.15  # 15% mahdollisuus löytää aarre
    robbed_chance = 0.10    # 10% mahdollisuus tulla ryöstetyksi

    roll = random.random()
    if roll < treasure_chance:
        item = satunnainen_avain

        sql = "UPDATE game SET raha = raha + %s WHERE id = %s;"
        kursori = yhteys.cursor()
        kursori.execute(sql, (TREASURES[satunnainen_avain], 1))
        yhteys.commit()
        return f"Löysit aarteen: {item} joka on {TREASURES[satunnainen_avain]}€ arvoinen! Summa talletetaan tilillesi"

    elif roll < treasure_chance + robbed_chance:

        sql = "UPDATE game SET raha = raha * 0.9 WHERE id = 1;"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        yhteys.commit()
        return "Ryöstö! Menetit 10% rahoistasi."
    else:
        return "Ei tapahtumaa."

#funktion suoritus
# tapahtuma = airport_event()

# print(f"Saavuit lentokentälle: {airport}")
# print(f"Tapahtuma: {tapahtuma}")