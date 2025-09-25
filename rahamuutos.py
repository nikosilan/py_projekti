import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='Juuso',
    password='salasana',
    autocommit=True
)

# päivittää rahasaldoa tietokantaan
def raha_muutos(raha_muutos):
    sql = "UPDATE game SET raha = %s WHERE id = %s;"
    kursori = yhteys.cursor()
    kursori.execute(sql, (raha_muutos, 1))
    return kursori.rowcount

# hakee tiedon paljon sinulla on rahaa tilillä
def raha_saldo():
    sql = "SELECT raha FROM game WHERE id = 1;"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    return print(tulos)



# kysyy paljon rahaa lisätään tilille. Myöhemmin tapahtuu proseduraalisesti.
raha_määrä = int(input("syötä rahan määrä: "))
raha_muutos(raha_määrä)
raha_saldo()