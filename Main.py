lentokentat = ["Helsinki", "Tampere", "Turku", "Oulu", "Rovaniemi"]

# Reitit
reitit = {
    "Helsinki": ["Tampere", "Turku", "Oulu"],
    "Tampere": ["Helsinki", "Oulu"],
    "Turku": ["Helsinki", "Rovaniemi"],
    "Oulu": ["Helsinki", "Tampere", "Rovaniemi"],
    "Rovaniemi": ["Turku", "Oulu"]
}

print("Tervetuloa tekstipohjaiseen lentopeliin!")
print("Lentokentät ja niiden reitit:")
for kentta, kohteet in reitit.items():
    print(f"{kentta} -> {', '.join(kohteet)}")

# Pelaajan aloituskenttä
nykyinen_kentta = input("\nValitse lähtökenttä: ").title()

while True:
    print(f"\nOlet nyt: {nykyinen_kentta}")
    print(f"Voit lentää seuraaviin kenttiin: {', '.join(reitit[nykyinen_kentta])}")
    
    kohde = input("Valitse minne haluat lentää (tai kirjoita 'lopeta'): ").title()
    
    if kohde.lower() == "lopeta":
        print("Peli päättyy. Kiitos pelaamisesta!")
        break
    
    if kohde in reitit[nykyinen_kentta]:
        print(f"Lennät {nykyinen_kentta} -> {kohde} ✈️")
        nykyinen_kentta = kohde
    else:
        print("Ei ole suoraa reittiä tähän kenttään. Valitse toinen.")
