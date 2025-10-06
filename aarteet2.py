import random


#aarteet ja niiden arvot

TREASURES = {"€10 seteli": 10,
             "€20 seteli": 20,
             "koru": 50,
             "matkamuisto": 200}

treasures_avaimet = ["€10 seteli", "€20 seteli", "koru", "matkamuisto"]
random.shuffle(treasures_avaimet)
satunnainen_avain = treasures_avaimet[0]

#määritellään tapahtumien mahdollisuudet

def airport_event(yhteys):
    treasure_chance = 0.15  
    robbed_chance = 0.10    

#arvotaan 
    roll = random.random()
    if roll < treasure_chance:
        item = satunnainen_avain

        #päivitetän rahasaldo tietokantaan
        sql = "UPDATE game SET raha = raha + %s WHERE id = %s;"
        kursori = yhteys.cursor()
        kursori.execute(sql, (TREASURES[satunnainen_avain], 1))
        yhteys.commit()
        tulos = print(f"Löysit aarteen: {item} joka on {TREASURES[satunnainen_avain]}€ arvoinen! Summa talletetaan tilillesi")
        return tulos

    elif roll < treasure_chance + robbed_chance:
        #päivitetään raha 10% pienemmäksi
        sql = "UPDATE game SET raha = raha * 0.9 WHERE id = 1;"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        yhteys.commit()
        tulos = print("Ryöstö! Menetit 10% rahoistasi.")
        return tulos
    else:
        tulos = print("Ei satunnaista tapahtumaa.")
        return tulos

