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

# --- Only ONE aircraft ---
aircraft = "Boeing 737"
aircraft_fuel_burn = 2600   # liters per 100 km

# --- Emission constants ---
FUEL_DENSITY = 0.8          # kg per liter
CO2_EMISSION_FACTOR = 3.16  # kg CO₂ per kg fuel


def get_airport_info(icao_code, conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT ident, name, iso_country, latitude_deg, longitude_deg
        FROM airport
        WHERE ident = %s
    """, (icao_code,))
    result = cursor.fetchone()
    cursor.close()
    return result  # (icao, name, country, lat, lon)

def get_current_fuel(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT bensa FROM game WHERE id = 1")
    result = cursor.fetchone()
    cursor.close()
    return result[0] if result else None

def update_fuel(conn, fuel_change):
    cursor = conn.cursor()
    current_fuel = get_current_fuel(conn)
    if current_fuel is None:
        print("Player not found in DB.")
        cursor.close()
        return False

    new_fuel = current_fuel + fuel_change
    MAX_BENSA = 240000
    MIN_BENSA = 0
    new_fuel = max(MIN_BENSA, min(MAX_BENSA, new_fuel))

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
            destinations.append(tulos)  # (icao, name, country, lat, lon)
    return destinations

def tulosta_numeroitu_lista(lista):
    for i, (_, name, country, _, _) in enumerate(lista, start=1):
        print(f"{i}. {name} in {country}")

# --- Main Game ---
def peli(yhteys):
    # Fetch starting airport EFHK
    current_airport = get_airport_info("EFHK", yhteys)
    if not current_airport:
        print("Error: EFHK not found in database!")
        return

    total_distance = 0
    flights = 0
    total_emissions = 0

    print(f"🌍 Welcome! Starting at {current_airport[1]} ({current_airport[0]}) in {current_airport[2]}.")
    print(f"Your aircraft: {aircraft}\n")

    while True:
        # Show random destinations
        kohteet = random_kohteet(yhteys)
        tulosta_numeroitu_lista(kohteet)

        choice = input("\nChoose destination (1-3) or q to quit: ")
        if choice.lower() == "q":
            print(f"\nGame over! Flights: {flights}, Total distance: {total_distance:.1f} km")
            print(f"Total CO₂ emissions: {total_emissions:.1f} kg")
            break

        try:
            choice = int(choice)
            if 1 <= choice <= 3:
                valittu = kohteet[choice - 1]
                icao, name, country, lat, lon = valittu

                coords_current = (current_airport[3], current_airport[4])
                coords_dest = (lat, lon)
                distance = geodesic(coords_current, coords_dest).kilometers

                fuel_needed = (distance / 100) * aircraft_fuel_burn
                current_fuel = get_current_fuel(yhteys)
                if current_fuel is None:
                    print("Player fuel not found in DB.")
                    break

                if fuel_needed > current_fuel:
                    print("Not enough fuel for this flight!")
                    continue

                update_fuel(yhteys, -fuel_needed)


                print(f"\n Flight {flights+1}:")
                print(f"Etäisyys {current_airport[1]} ja {name} airportin välillä on {distance:.1f} km")
                print(f"   Käytetty polttoaine: {fuel_needed:.1f} litraa ({aircraft})")

                # Emissions calculation
                fuel_needed_kg = fuel_needed * FUEL_DENSITY
                co2_emissions = fuel_needed_kg * CO2_EMISSION_FACTOR
                print(f"   Arvioidut CO₂-päästöt: {co2_emissions:.1f} kg")

                total_distance += distance
                total_emissions += co2_emissions
                flights += 1
                current_airport = valittu
            else:
                print("Choose 1, 2, or 3.")
        except ValueError:
            print("Enter a number (1-3) or q to quit.")

# Start Game
peli(yhteys)
