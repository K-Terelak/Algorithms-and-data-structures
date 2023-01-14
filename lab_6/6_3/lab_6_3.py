import lab_6.FileHandler as FH
import time


def quickSort(dane, lewo, prawo):
    if lewo >= prawo:
        return
    pivot = dane[(lewo + prawo) // 2]
    x = lewo - 1
    y = prawo + 1
    while True:
        while True:
            x += 1
            if dane[x] >= pivot:
                break
        while True:
            y -= 1
            if dane[y] <= pivot:
                break
        if x >= y:
            break
        dane[x], dane[y] = dane[y], dane[x]
    quickSort(dane, lewo, y)
    quickSort(dane, y + 1, prawo)


zbior = "duzy"

start = time.time()
dane = FH.pobieranieDanych(zbior)
quickSort(dane, 0, len(dane) - 1)
stop = time.time()

print(f"Czas wykonywania: {stop - start}s")

FH.zapisywanieDanych(f"wynikQuick{zbior.capitalize()}", dane)
