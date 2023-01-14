def pobieranieDanych(plik):
    dane = []
    with open(f"../zbiory/{plik}Zbior.txt", "r") as p:
        for line in p:
            dane.append(int(line))

    return dane


def zapisywanieDanych(plik, dane):
    with open(f"../wyniki/{plik}.txt", "w") as wynik:
        for element in dane:
            wynik.write(f"{str(element)}\n")
