def naive(text, pattern):
    for x in range(len(text) - len(pattern) + 1):
        y = 0
        while y < len(pattern):
            if text[x + y] != pattern[y]:
                break
            y += 1
        if y == len(pattern):
            print("Found pattern starting on index:", x)


t = "ABBABCDAABABCAABAAADDABA"
p = "ABA"
naive(t, p)
