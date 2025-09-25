import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='Juuso',
    password='salasana',
    autocommit=True
)


def bensa_muutos(bensa_määrä):

    sql = "UPDATE game SET bensa = %s WHERE id = 1"
    kursori = yhteys.cursor()
    kursori.execute(sql, (bensa_määrä,))
    yhteys.commit()
    print("Fuel updated successfully.")


#bensa_määrä = float(input("How much fuel: "))
#bensa_muutos(bensa_määrä)


#tulosta_numeroitu_lista()
def tankissa_bensa():
    sql = "SELECT bensa FROM game WHERE id = 1;"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    if tulos:
        print(tulos[0])
    else:
        print("No data found")
tankissa_bensa()


