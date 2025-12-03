# import mysql.connector
# from aircraft_lista import search_for_open_destinations
import random
import time

# -----------------------------
# GameState (get_flight_count, update_flight_count, random_destination, search_for_open_destinations, tulosta_numeroitu_lista, nimea_hahmo, raha_muutos, raha_saldo)
# -----------------------------

class GameState:
    @staticmethod
    def get_flight_count(yhteys, hahmo_id=1):
        kursori = yhteys.cursor()
        sql = "SELECT flights FROM game WHERE id = %s"
        kursori.execute(sql, (hahmo_id,))
        result = kursori.fetchone()
        kursori.close()
        if result:
            return result[0]

    @staticmethod
    def update_flight_count(yhteys, flight_count, hahmo_id=1):
        kursori = yhteys.cursor()
        sql = "UPDATE game SET flights = %s WHERE id = %s"
        kursori.execute(sql, (flight_count, hahmo_id))
        yhteys.commit()
        kursori.close()
        return kursori.rowcount  # returns number of rows updated

    @staticmethod
    def random_destination(yhteys, flight_count):
        destinations = []
        continents_sql_list = set()

        avatut_maanosat = GameState.search_for_open_destinations(flight_count)
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

    @staticmethod
    def search_for_open_destinations(flight_count):
        # määrittelee, mitkä maanosat ovat avoinna lentojen määrän perusteella
        maanosat_jarjestys = ["EU", "NA", "SA", "AS", "OC", "AF", "AN"]
        avattujen_maara = min((flight_count // 5) + 1, len(maanosat_jarjestys))
        # palauttaa listan avoinna olevista maanosista
        return maanosat_jarjestys[:avattujen_maara]

    @staticmethod
    def tulosta_numeroitu_lista(lista):
        # tulostaa lentokonelistan numeroituna
        for indeksi, (_, alkio, maanimi, _, _) in enumerate(lista, start=1):
            print(f"{indeksi}. {alkio} in {maanimi}")
        return

    @staticmethod
    def nimea_hahmo(yhteys, nimi, hahmo_id=1):
        """
        Luo tai päivittää pelihahmon.
        Nimeää pelihahmon tietokantaan annetulla yhteydellä.
        Katkaisee nimen, jos se on liian pitkä sarakkeelle screen_name.
        Palauttaa päivitettyjen rivien määrän.
        Asettaa bensa=240000 ja raha=100 aloitusarvoiksi.
        """
        max_pituus = 20
        if len(nimi) > max_pituus:
            print(f"Nimi on liian pitkä, se katkaistaan {max_pituus} merkkiin.")
            nimi = nimi[:max_pituus]

        kursori = yhteys.cursor()

        # Lisää tai päivitä pelaaja id=1
        # INSERT INTO on melko sama kuin UPDATE
        # ON DUPLICATE KEY UPDATE tarkoittaa jos on olemassa jo id=1 pelaaja, se poistetaan ja luodaan uusi pelaaja
        sql = ("INSERT INTO game (id, screen_name, bensa, raha, flights, sijainti) "
               "VALUES (%s, %s, %s, %s, %s, %s) "
               "ON DUPLICATE KEY UPDATE "
               "screen_name = VALUES(screen_name), "
               "bensa = VALUES(bensa), "
               "raha = VALUES(raha), "
               "flights = VALUES(flights), "
               "sijainti = VALUES(sijainti);")
        kursori.execute(sql, (hahmo_id, nimi, 240000, 100, 0, "EFHK"))

        yhteys.commit()
        print(f"Player '{nimi}' created/updated: 240000 fuel, 100€ money and 0 flights.")
        return kursori.rowcount

    # päivittää rahasaldoa tietokantaan
    @staticmethod
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
    @staticmethod
    def raha_saldo(yhteys):
        sql = "SELECT raha FROM game WHERE id = 1;"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchone()
        if tulos is None:
            return 0
        return tulos[0]


# -----------------------------
# AIRPORT (get_airport_info, get_current_airport, update_current_airport, get_current_fuel, update_fuel)
# -----------------------------

class Airport:
    @staticmethod
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

    @staticmethod
    def get_current_airport(yhteys, hahmo_id=1):
        cursor = yhteys.cursor()
        sql = """
              SELECT airport.ident, airport.name, country.name, airport.latitude_deg, airport.longitude_deg
              FROM game
                       JOIN airport ON game.sijainti = airport.ident
                       JOIN country ON airport.iso_country = country.iso_country
              WHERE game.id = %s \
              """
        cursor.execute(sql, (hahmo_id,))
        result = cursor.fetchone()
        cursor.close()
        return result

    @staticmethod
    def update_current_airport(yhteys, uusi_icao, hahmo_id=1):
        cursor = yhteys.cursor()
        sql = "UPDATE game SET sijainti = %s WHERE id = %s"
        cursor.execute(sql, (uusi_icao, hahmo_id))
        yhteys.commit()
        cursor.close()

    @staticmethod
    def get_current_fuel(conn):
        cursor = conn.cursor()
        cursor.execute("SELECT bensa FROM game WHERE id = 1")
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else None

    @staticmethod
    def update_fuel(conn, fuel_change, min_fuel=0, max_fuel=240000):
        cursor = conn.cursor()
        current_fuel = Airport.get_current_fuel(conn)
        if current_fuel is None:
            print("Player not found in DB.")
            cursor.close()
            return False

        new_fuel = max(min_fuel, min(max_fuel, current_fuel + fuel_change))
        cursor.execute("UPDATE game SET bensa = %s WHERE id = 1", (new_fuel,))
        conn.commit()
        cursor.close()
        print(f"Fuel updated: {current_fuel:.2f} → {new_fuel:.2f} liters")
        return True


# -----------------------------
# MINIGAMES (noppa_peli, tietokilpailu_peli)
# -----------------------------

class Minigames:
    @staticmethod
    def noppa_peli(pisteet):
        tietokone_noppa1 = random.randint(1, 6)
        tietokone_noppa2 = random.randint(1, 6)

        print(f"Tietokone heitti: {tietokone_noppa1} ja {tietokone_noppa2}")
        time.sleep(1.5)

        while True:
            syote = input("Haluatko heittää noppia? (y/n): ").lower()

            if syote == "y":
                pelaaja_noppa1 = random.randint(1, 6)
                pelaaja_noppa2 = random.randint(1, 6)

                print(f"Sinun heittosi: {pelaaja_noppa1} ja {pelaaja_noppa2}")

                if ((pelaaja_noppa1, pelaaja_noppa2) == (tietokone_noppa1, tietokone_noppa2)
                        or (pelaaja_noppa2, pelaaja_noppa1) == (tietokone_noppa1, tietokone_noppa2)):
                    palkinto = random.randint(1, 100)
                    print(f"Onnittelut! Heitot täsmäsivät, saat {palkinto}€!")
                    return palkinto
                else:
                    print("Heitot eivät täsmänneet, ei rahaa.")

            elif syote == "n":
                print("Et halunnut heittää noppia, peli päättyi.")
                return pisteet
            else:
                print("Väärä syöte, anna 'y' tai 'n'.")

    @staticmethod
    def tietokilpailu_peli(pisteet):
        saatu_pisteet = 0  # se on väliaikainen asia, joka sitten näyttää pelin lopussa saatu pisteet
        # 1 piste = 1 euro
        tietopankki = {
            "Kuinka monta maanosaa maailmassa on?": "7",
            "Mikä on maailman suurin valtameri?": "Tyynimeri",
            "Mikä on veden kemiallinen kaava?": "H2O",
            "Mikä on Suomen pääkaupunki?": "Helsinki",
            "Mikä planeetta tunnetaan punaisena planeettana?": "Mars",
            "Kuka maalasi Mona Lisan?": "Leonardo da Vinci",
            "Mikä on maailman korkein vuori?": "Mount Everest",
            "Mikä on maailman nopein maaeläin?": "Gepardi",
            "Mikä kieli on eniten puhuttu maailmassa?": "Mandariinikiina",
            "Minkä komediaryhmän mukaan Python-ohjelma on nimetty?": "Monty Python",
            "Mikä eläin pyton on?": "käärme",
            "Kumpi on tilastollisesti turvallisempi matkustamisen muoto, lentäminen vai autolla ajaminen?": "lentäminen",
            "Millä sanalla Pythonissa aloitetaan ehtolause?": "if",
            "Missä kaupungissa sijaitsee Eiffel-torni?": "ranska",
            "Minkä maan pääkaupunki on Oslo?": "norja"
        }

        kysymykset = list(tietopankki.items())

        # Valitaan 3 satunnaista kysymystä
        satunnaiset_kysymykset = random.sample(kysymykset, 3)

        for kysymys, oikea_vastaus in satunnaiset_kysymykset:
            print(kysymys)
            pelaajan_vastaus = input("Anna vastaus: ").strip()
            if pelaajan_vastaus.lower() == oikea_vastaus.lower():
                random_piste_maara = random.randint(1, 100)
                print(f"Onnea! Vastasit oikein ja ansaitset {random_piste_maara}€.")
                pisteet += random_piste_maara
                saatu_pisteet += random_piste_maara
            else:
                print("Valitettavasti et päässyt läpi ja et ansainnut senttiäkään!")
                break

        print(f"\nPelin lopussa sinulla on yhteensä {saatu_pisteet}€.")
        return saatu_pisteet


# -----------------------------
# EVENTS (airport_event, airport_huolto)
# -----------------------------

TREASURES = {"€10 seteli": 10,
                 "€20 seteli": 20,
                 "koru": 50,
                 "matkamuisto": 200}

treasures_avaimet = ["€10 seteli", "€20 seteli", "koru", "matkamuisto"]
random.shuffle(treasures_avaimet)
satunnainen_avain = treasures_avaimet[0]

class Events:
    @staticmethod
    def airport_event(yhteys):
        treasure_chance = 0.15
        robbed_chance = 0.10

        # arvotaan
        roll = random.random()
        if roll < treasure_chance:
            item = satunnainen_avain

            # päivitetän rahasaldo tietokantaan
            sql = "UPDATE game SET raha = raha + %s WHERE id = %s;"
            kursori = yhteys.cursor()
            kursori.execute(sql, (TREASURES[satunnainen_avain], 1))
            yhteys.commit()
            tulos = print(
                f"Löysit aarteen: {item} joka on {TREASURES[satunnainen_avain]}€ arvoinen! Summa talletetaan tilillesi")
            return tulos

        elif roll < treasure_chance + robbed_chance:
            # päivitetään raha 10% pienemmäksi
            sql = "UPDATE game SET raha = raha * 0.9 WHERE id = 1;"
            kursori = yhteys.cursor()
            kursori.execute(sql)
            yhteys.commit()
            tulos = print("Ryöstö! Menetit 10% rahoistasi.")
            return tulos
        else:
            tulos = print("Ei satunnaista tapahtumaa.")
            return tulos

    @staticmethod
    def aircraft_huolto(yhteys):
        """Arpoo satunnaisen lentokonehuollon ja tulostaa, mikä huolto tehtiin."""

        # Todennäköisyys, että huolto tapahtuu (esim. 30 %)
        huolto_mahdollisuus = 0.8

        if random.random() > huolto_mahdollisuus:
            tulos = print("🛠️ Lentokone on hyvässä kunnossa — ei huoltoa tällä kertaa!\n")
            return tulos

        # Lista mahdollisista huolloista (nimi, todennäköisyys)
        huollot = [
            ("✈️ Moottorin tarkastus", 0.5),
            ("🔧 Öljynvaihto", 0.5),
            ("🛞 Renkaiden tarkistus", 0.5),
            ("💨 Polttoainejärjestelmän puhdistus", 0.5),
            ("⚙️ Hydraulijärjestelmän huolto", 0.5),
            ("🧰 Täydellinen huolto", 0.5)
        ]

        # Arvotaan huolto todennäköisyyksien mukaan
        r = random.random()
        cumulative = 0.0
        for nimi, todennakoisyys in huollot:
            cumulative += todennakoisyys
            if r <= cumulative:
                print(f"🔩 Huolto tehtiin: {nimi}\n")
                time.sleep(2)
                return

        # Jos mikään huolto ei osu
        print("🛠️ Ei huoltoa tällä kertaa.\n")


class GameSession:
    def __init__(self):
        self.output_buffer = []
        self.current_choices = []
        self.input_buffer = []

    def write(self, message):
        self.output_buffer.append(message)

    def get_output(self):
        out = "\n".join(self.output_buffer)
        self.output_buffer.clear()
        return out

    def set_choices(self, choices):
        self.current_choices = choices

    def get_choices(self):
        return self.current_choices

    def store_input(self, value):
        self.input_buffer.append(value)

    def get_input(self):
        if self.input_buffer:
            return self.input_buffer.pop(0)
        return None

    def wait_for_input(self):
        value = self.get_input()
        while value is None:
            time.sleep(0.1)
            value = self.get_input()
        return value

session = GameSession()