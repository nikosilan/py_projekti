''' Käyttäkää näitä jos haluatte saada yhteyden tietokantaan '''
# from log_in import kirjautuminen
# yhteys = kirjautuminen()

def nimea_hahmo(yhteys, nimi, hahmo_id=1):
    """
    Luo tai päivittää pelihahmon.
    Nimeää pelihahmon tietokantaan annetulla yhteydellä.
    Katkaisee nimen, jos se on liian pitkä sarakkeelle screen_name.
    Palauttaa päivitettyjen rivien määrän.
    Asettaa bensa=240000 ja raha=100 aloitusarvoiksi.
    """
    max_pituus = 20
    if len(nimi) > max_pituus:
        print(f"Nimi on liian pitkä, se katkaistaan {max_pituus} merkkiin.")
        nimi = nimi[:max_pituus]

    kursori = yhteys.cursor()

    # Lisää tai päivitä pelaaja id=1
    # INSERT INTO on melko sama kuin UPDATE
    # ON DUPLICATE KEY UPDATE tarkoittaa jos on olemassa jo id=1 pelaaja, se poistetaan ja luodaan uusi pelaaja
    sql = ("INSERT INTO game (id, screen_name, bensa, raha, flights) "
           "VALUES (%s, %s, %s, %s, %s) "
           "ON DUPLICATE KEY UPDATE "
           "screen_name = VALUES(screen_name), "
           "bensa = VALUES(bensa), "
           "raha = VALUES(raha), "
           "flights = VALUES(flights);")
    kursori.execute(sql, (hahmo_id, nimi, 240000, 100, 0))

    yhteys.commit()
    print(f"Player '{nimi}' created/updated: 240000 fuel, 100€ money and 0 flights.")
    return kursori.rowcount

#   Tämä voi laittaa pääohjelmaan
# nimi = input("Syötä oma nimi: ")
# nimea_hahmo(yhteys, nimi)