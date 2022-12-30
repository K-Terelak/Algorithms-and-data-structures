alphabet_number = 256


def badCharacterHeuristic(string, size):
    badCharacter = [-1] * alphabet_number
    for i in range(size):
        badCharacter[ord(string[i])] = i
    return badCharacter


def boyerMoore(text, pattern):
    badCharacter = badCharacterHeuristic(pattern, len(pattern))
    s = 0

    while s <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            print("Found pattern starting on index: " + str(s))
            if s + len(pattern) < len(text):
                s += (len(pattern) - badCharacter[ord(text[s + len(pattern)])])
            else:
                s += 1
        else:
            s += max(1, j - badCharacter[ord(text[s + j])])


t = "ABBABCDAABABCAABAAADDABA"
p = "ABA"
boyerMoore(t, p)
