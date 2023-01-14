import lab_6.FileHandler as FH
import time

def insertionSort(dane):
    for x in range(1, len(dane)):
        znak = dane[x]
        y = x - 1
        while y >= 0 and znak < dane[y]:
            dane[y + 1] = dane[y]
            y -= 1
        dane[y + 1] = znak

    return dane


zbior = "duzy"

start = time.time()
wynik = insertionSort(FH.pobieranieDanych(zbior))
stop = time.time()

print(f"Czas wykonywania: {stop-start}s")


FH.zapisywanieDanych(f"wynikInsert{zbior.capitalize()}", wynik)
