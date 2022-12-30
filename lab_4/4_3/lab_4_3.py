alphabet_amount = 256


def karpRabin(text, pattern, prime):
    j = 0
    i = 0
    p = 0
    t = 0
    h = 1

    for i in range(len(pattern) - 1):
        h = (h * alphabet_amount) % prime

    for i in range(len(pattern)):
        p = (alphabet_amount * p + ord(pattern[i])) % prime
        t = (alphabet_amount * t + ord(text[i])) % prime

    for i in range(len(text) - len(pattern) + 1):
        if p == t:
            for j in range(len(pattern)):
                if text[i + j] != pattern[j]:
                    break

            j += 1
            if j == len(pattern):
                print("Found pattern starting on index: " + str(i))

        if i < len(text) - len(pattern):
            t = (alphabet_amount * (t - ord(text[i]) * h) + ord(text[i + len(pattern)])) % prime
            if t < 0:
                t = t + prime


t = "ABBABCDAABABCAABAAADDABA"
p = "ABA"
karpRabin(t, p, 3)
