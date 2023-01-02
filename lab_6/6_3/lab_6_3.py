def quick_sort(tab, left, right):
    if left >= right:
        return
    pivot = tab[(left + right) // 2]
    i = left - 1
    j = right + 1
    while True:
        while True:
            i += 1
            if tab[i] >= pivot:
                break
        while True:
            j -= 1
            if tab[j] <= pivot:
                break
        if i >= j:
            break
        tab[i], tab[j] = tab[j], tab[i]
    quick_sort(tab, left, j)
    quick_sort(tab, j + 1, right)


arr = [2, 1, 3, 7, 6, 7, 4, 9]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
