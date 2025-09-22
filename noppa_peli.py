import random

def heitä_noppa(syote):
    if syote.lower() == "noppa":
        noppa_1 = int(random.randint(1, 6))
        noppa_2 = int(random.randint(1, 6))
        tulos = f'Heitetty {noppa_1} ja {noppa_2}'
        print(tulos)
    else:
        print("Anna tietty komento.")
    return tulos

def main():
    syote = input("Anna komento (noppa): ")
    heitä_noppa(syote)

if __name__ == "__main__":
    main()