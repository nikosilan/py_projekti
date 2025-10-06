import mysql.connector
from aircraft_lista import search_for_open_destinations


def get_flight_count(yhteys, hahmo_id=1):
    kursori = yhteys.cursor()
    sql = "SELECT flights FROM game WHERE id = %s"
    kursori.execute(sql, (hahmo_id,))
    result = kursori.fetchone()
    kursori.close()
    if result:
        return result[0]

def update_flight_count(yhteys, flight_count, hahmo_id=1):
    kursori = yhteys.cursor()
    sql = "UPDATE game SET flights = %s WHERE id = %s"
    kursori.execute(sql, (flight_count, hahmo_id))
    yhteys.commit()
    kursori.close()
    return kursori.rowcount  # returns number of rows updated


def get_airport_info(icao_code, conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT ident, name, iso_country, latitude_deg, longitude_deg
        FROM airport
        WHERE ident = %s
    """, (icao_code,))
    result = cursor.fetchone()
    cursor.close()
    return result

def get_current_fuel(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT bensa FROM game WHERE id = 1")
    result = cursor.fetchone()
    cursor.close()
    return result[0] if result else None

def update_fuel(conn, fuel_change, min_fuel=0, max_fuel=240000):
    cursor = conn.cursor()
    current_fuel = get_current_fuel(conn)
    if current_fuel is None:
        print("Player not found in DB.")
        cursor.close()
        return False

    new_fuel = max(min_fuel, min(max_fuel, current_fuel + fuel_change))
    cursor.execute("UPDATE game SET bensa = %s WHERE id = 1", (new_fuel,))
    cursor.close()
    print(f"Fuel updated: {current_fuel:.2f} → {new_fuel:.2f} liters")
    return True

def random_destination(yhteys, flight_count):
    destinations = []
    continents_sql_list = set()

    avatut_maanosat = search_for_open_destinations(flight_count)
    continents_sql_list.update(avatut_maanosat)

    continents_str = ','.join(f"'{c}'" for c in continents_sql_list)

    print("Avatut maanosat:", ", ".join(continents_sql_list))

    for kohde in range(3):
        sql = (f'SELECT airport.ident, airport.name, country.name, airport.latitude_deg, airport.longitude_deg '
               f'FROM airport '
               f'INNER JOIN country ON airport.iso_country = country.iso_country '
               f'WHERE country.continent IN ({continents_str})'
               f'AND TYPE like "large_airport" ORDER BY RAND() LIMIT 1;')

        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchone()

        # Purkaa monikon ja lisää kenttien ja maiden nimet listaan destinations
        if tulos:
            destinations.append(tulos)

    return destinations
