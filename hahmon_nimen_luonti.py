import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='Juuso',
    password='salasana',
    autocommit=True
)

hahmon_id = 1
hahmon_nimi = input("Nimeä hahmo (pelkkä etumimi/käyttäjänimi): ").strip()

# Nimeää pelihahmon käyttäjän syötteellä. Funktio palauttaa muutettujen rivien arvon
def nimea_hahmo(nimi):
    sql = "UPDATE game SET screen_name = %s WHERE id = %s;"
    kursori = yhteys.cursor()
    kursori.execute(sql, (nimi, hahmon_id))
    return kursori.rowcount

# Sijoittaa nimen funktioon ja tallentaa päivitettyjen rivien määrän muuttujaan.
tulos = nimea_hahmo(hahmon_nimi)

# Testsaa ja ilmoittaa onnistuiko tietokannan päivitys
if tulos == 1:
    print(f"Hahmosi nimi on: {hahmon_nimi}")
else:
    print("Nimen päivitys ei onnistunut.")