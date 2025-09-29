# hahmo.py
def nimea_hahmo(yhteys, nimi, hahmo_id=1):
    """
    Nimeää pelihahmon tietokantaan annetulla yhteydellä.
    Katkaisee nimen, jos se on liian pitkä sarakkeelle screen_name.
    Palauttaa päivitettyjen rivien määrän.
    """
    max_pituus = 20  # riippuu tietokannan screen_name-sarakkeesta
    if len(nimi) > max_pituus:
        print(f"Nimi on liian pitkä, se katkaistaan {max_pituus} merkkiin.")
        nimi = nimi[:max_pituus]

    sql = "UPDATE game SET screen_name = %s WHERE id = %s;"
    kursori = yhteys.cursor()
    kursori.execute(sql, (nimi, hahmo_id))
    yhteys.commit()
    return kursori.rowcount