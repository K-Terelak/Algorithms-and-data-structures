import lab_6.FileHandler as FH
import time


def bubbleSort(dane):
    for x in range(len(dane) - 1):
        for y in range(len(dane) - x - 1):
            if dane[y] > dane[y + 1]:
                dane[y], dane[y + 1] = dane[y + 1], dane[y]

    return dane


zbior = "duzy"

start = time.time()
wynik = bubbleSort(FH.pobieranieDanych(zbior))
stop = time.time()

print(f"Czas wykonywania: {stop - start}s")

FH.zapisywanieDanych(f"wynikBubble{zbior.capitalize()}", wynik)
