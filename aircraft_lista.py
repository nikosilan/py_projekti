def tulosta_numeroitu_lista(lista):
    for i, (_, name, country, _, _) in enumerate(lista, start=1):
        print(f"{i}. {name} in {country}")
