import mysql.connector
from log_in import kirjautuminen

#yhteys = kirjautuminen()


# päivittää rahasaldoa tietokantaan
def raha_muutos(yhteys, raha_muutos):
    sql = "UPDATE game SET raha = raha + %s WHERE id = %s;"
    kursori = yhteys.cursor()
    kursori.execute(sql, (raha_muutos, 1))
    return kursori.rowcount

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


