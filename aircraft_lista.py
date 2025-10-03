def tulosta_numeroitu_lista(lista):
    for indeksi, (_, alkio, maanimi, _, _) in enumerate(lista, start=1):
        print(f"{indeksi}. {alkio} in {maanimi}")
    return

def search_for_open_destinations(flight_count):
    maanosat_jarjestys = ["EU", "NA", "SA", "AS", "OC", "AF", "AN"]
    avattujen_maara = min((flight_count // 5) + 1, len(maanosat_jarjestys))
    return maanosat_jarjestys[:avattujen_maara]