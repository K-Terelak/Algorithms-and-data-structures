import lab_6.FileHandler as FH
import time


def mergeSort(dane):
    if len(dane) > 1:

        srodek = len(dane) // 2
        lewo = dane[:srodek]
        prawo = dane[srodek:]

        mergeSort(lewo)
        mergeSort(prawo)

        x = 0
        y = 0
        z = 0
        while x < len(lewo) and y < len(prawo):
            if lewo[x] <= prawo[y]:
                dane[z] = lewo[x]
                x += 1
            else:
                dane[z] = prawo[y]
                y += 1
            z += 1

        while x < len(lewo):
            dane[z] = lewo[x]
            x += 1
            z += 1

        while y < len(prawo):
            dane[z] = prawo[y]
            y += 1
            z += 1

    return dane


zbior = "maly"

start = time.time()
wynik = mergeSort(FH.pobieranieDanych(zbior))
stop = time.time()

print(f"Czas wykonywania: {stop - start}s")

FH.zapisywanieDanych(f"wynikMerge{zbior.capitalize()}", wynik)
