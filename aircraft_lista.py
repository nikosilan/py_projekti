def tulosta_numeroitu_lista(lista):
    #tulostaa lentokonelistan numeroituna
    for indeksi, (_, alkio, maanimi, _, _) in enumerate(lista, start=1):
        print(f"{indeksi}. {alkio} in {maanimi}")
    return

def search_for_open_destinations(flight_count):
    #määrittelee, mitkä maanosat ovat avoinna lentojen määrän perusteella
    maanosat_jarjestys = ["EU", "NA", "SA", "AS", "OC", "AF", "AN"]
    avattujen_maara = min((flight_count // 5) + 1, len(maanosat_jarjestys))
    #palauttaa listan avoinna olevista maanosista
    return maanosat_jarjestys[:avattujen_maara]