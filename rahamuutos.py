import mysql.connector
from log_in import kirjautuminen

#yhteys = kirjautuminen()


# päivittää rahasaldoa tietokantaan
def raha_muutos(yhteys, raha_muutos):
    kursori = yhteys.cursor()

    # varmista että raha ei ole NULL
    sql_select = "SELECT COALESCE(raha, 0) FROM game WHERE id = 1;"
    kursori.execute(sql_select)
    tulos = kursori.fetchone()
    nykyinen_raha = tulos[0] if tulos else 0

    uusi_raha = max(0, nykyinen_raha + raha_muutos)

    sql_update = "UPDATE game SET raha = %s WHERE id = 1;"
    kursori.execute(sql_update, (uusi_raha,))
    yhteys.commit()
    kursori.close()

# hakee tiedon paljon sinulla on rahaa tilillä
def raha_saldo(yhteys):
    sql = "SELECT raha FROM game WHERE id = 1;"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    if tulos is None:
        return 0
    return tulos[0]

# globaali muuttuja 'raha'
'''rahaa_tilillä = raha_saldo()'''


# Kysyy paljon rahaa lisätään tilille (tai otetaan pois). Myöhemmin tämä tapahtuu proseduraalisesti.


