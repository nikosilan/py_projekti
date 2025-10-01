import mysql.connector

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

def random_kohteet(conn):
    """Fetch 3 random large airports in Europe."""
    destinations = []
    for _ in range(3):
        sql = ("""
            SELECT airport.ident, airport.name, country.name, airport.latitude_deg, airport.longitude_deg
            FROM airport
            INNER JOIN country ON airport.iso_country = country.iso_country
            WHERE country.continent = 'EU' AND type LIKE 'large_airport'
            ORDER BY RAND() LIMIT 1;
        """)
        cursor = conn.cursor()
        cursor.execute(sql)
        tulos = cursor.fetchone()
        cursor.close()
        if tulos:
            destinations.append(tulos)
    return destinations
