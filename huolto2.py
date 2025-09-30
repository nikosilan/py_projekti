import random

def korjaus():
    """
    Huoltaa lentokonetta ja palauttaa tiedon mitä korjattiin.
    """
    korjattavat = ["moottori", "siivet", "ohjausjärjestelmä", "rungon tarkastus"]
    korjattu_osio = random.choice(korjattavat)
    return f"Huolto: Lentokoneesi {korjattu_osio} on tarkastettu ja korjattu."

def tankkaus(fuel_level):
    """
    Tankkaa lentokonetta. Palauttaa uuden polttoainearvon ja viestin.
    """
    lisays = 20
    uusi_fuel = min(100, fuel_level + lisays)
    return uusi_fuel, f"Tankkaus: Polttoainetta lisättiin {lisays} yksikköä. Uusi taso: {uusi_fuel}%"

def airport_service_event(fuel_level):
    """
    Valitsee satunnaisesti tapahtuman: huolto, tankkaus tai ei tapahtumaa.
    """
    events = ["korjaus", "tankkaus", "ei_tapahtumaa"]
    weights = [0.4, 0.5, 0.1]  # Todennäköisyydet
    tapahtuma = random.choices(events, weights)[0]

    if tapahtuma == "korjaus":
        viesti = korjaus()
        return fuel_level, viesti
    elif tapahtuma == "tankkaus":
        uusi_fuel, viesti = tankkaus(fuel_level)
        return uusi_fuel, viesti
    else:
        return fuel_level, "Ei tapahtumaa."

# Pääohjelma
fuel_level = 50
airport = "Lontoo"

fuel_level, tapahtuma_viesti = airport_service_event(fuel_level)

print(f"Saavuit lentokentälle: {airport}")
print(f"Tapahtuma: {tapahtuma_viesti}")
print(f"Lentokoneen polttoaine: {fuel_level}%")
