from geopy.distance import geodesic
import mysql.connector
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='Daniel',
    password='DA10',
    autocommit=True
)

# oletetaan meillä on dictionary of aircraft bensan kulutus per 100 km
aircraft_fuel_burn = {
    "Cessna 172": 35,
    "Boeing 737": 2600,
    "Airbus A320": 2500,
    "Boeing 777": 7200,
    "ATR 72": 800
}

def get_airport_coordinates(icao_code, conn):
    cursor = conn.cursor()
    cursor.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s", (icao_code,))
    result = cursor.fetchone()
    cursor.close()
    return result

def get_current_fuel(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT bensa FROM game WHERE id = 1")
    result = cursor.fetchone()
    cursor.close()
    if result:
        return result[0]

def update_fuel(conn, fuel_change):
    cursor = conn.cursor()
    # Get current fuel first
    current_fuel = get_current_fuel(conn)
    if current_fuel is None:
        print("Player not found.")
        cursor.close()
        return False

    new_fuel = current_fuel + fuel_change
    MAX_BENSA = 240000
    MIN_BENSA = 0

    # Clamp fuel
    if new_fuel > MAX_BENSA:
        new_fuel = MAX_BENSA
    elif new_fuel < MIN_BENSA:
        new_fuel = MIN_BENSA

    cursor.execute("UPDATE game SET bensa = %s WHERE id = 1", (new_fuel,))
    cursor.close()
    print(f"Fuel updated: {current_fuel:.2f} liter is updated to {new_fuel:.2f} liters")
    return True

def fly_between_airports(conn):
    # pelaajan syöte(Mistä->mihin)
    icao1 = input("Enter departure airport ICAO code: ").upper()
    icao2 = input("Enter destination airport ICAO code: ").upper()
    print("Available aircraft:")
    for plane in aircraft_fuel_burn:
        print(f"- {plane}")
    aircraft = input("Choose aircraft from the above list: ")

    if aircraft not in aircraft_fuel_burn:
        print("Invalid aircraft choice.")
        return

    coords1 = get_airport_coordinates(icao1, conn)
    coords2 = get_airport_coordinates(icao2, conn)

    if not coords1 or not coords2:
        print("One or both ICAO codes are invalid.")
        return

    distance_km = geodesic(coords1, coords2).kilometers
    print(f"Distance between {icao1} and {icao2}: {round(distance_km, 2)} km")

    fuel_needed = (distance_km / 100) * aircraft_fuel_burn[aircraft]
    print(f"Fuel needed for the flight with {aircraft}: {round(fuel_needed, 2)} liters")

    current_fuel = get_current_fuel(conn)
    if current_fuel is None:
        print("Player not found.")
        return

    if fuel_needed > current_fuel:
        print("Not enough fuel to make this flight.")
        return

    # vähennetään käytetty bensaa
    success = update_fuel(conn, -fuel_needed)
    if success:
        print("Flight completed successfully!")
    else:
        print("Error updating fuel.")


fly_between_airports(yhteys)
