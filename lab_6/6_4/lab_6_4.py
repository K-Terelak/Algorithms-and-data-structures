import lab_6.FileHandler as FH
import time


def heapify(dane, n, x):
    najwiekszy = x
    lewo = 2 * x + 1
    prawo = 2 * x + 2

    if lewo < n and dane[x] < dane[lewo]:
        najwiekszy = lewo

    if prawo < n and dane[najwiekszy] < dane[prawo]:
        najwiekszy = prawo

    if najwiekszy != x:
        dane[x], dane[najwiekszy] = dane[najwiekszy], dane[x]
        heapify(dane, n, najwiekszy)


def heapSort(dane):
    for x in range(len(dane) // 2, -1, -1):
        heapify(dane, len(dane), x)

    for x in range(len(dane) - 1, 0, -1):
        dane[x], dane[0] = dane[0], dane[x]
        heapify(dane, x, 0)
    
    return dane


zbior = "maly"

start = time.time()
wynik = heapSort(FH.pobieranieDanych(zbior))
stop = time.time()

print(f"Czas wykonywania: {stop - start}s")

FH.zapisywanieDanych(f"wynikHeap{zbior.capitalize()}", wynik)
