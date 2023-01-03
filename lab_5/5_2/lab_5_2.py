code = {"A": "", "B": "", "C": "", "D": "", "E": "", "F": "", "G": "", "H": "", "I": "", "J": "", "K": "", "L": "",
        "M": "", "N": "", "O": "", "P": "", "R": "", "S": "", "T": "", "U": "", "W": "", "Y": "", "Z": ""}


def huffman(symbols, text):
    symbols = sorted(symbols, reverse=True)
    while len(symbols) > 1:
        s1 = symbols.pop()
        s2 = symbols.pop()
        for char in s1[1]:
            code[char] = "0" + code[char]
        for char in s2[1]:
            code[char] = "1" + code[char]
        s1s2 = (s1[0] + s2[0], s1[1] + s2[1])
        symbols.append(s1s2)
        symbols = sorted(symbols, reverse=True)
    for entry in code:
        if code[entry] != "":
            print(f"{entry} - {code[entry]}")

    print(f"Text: {text}")
    print("Encoded: ", end="")
    for char in text:
        print(code[char], end="")


t = "ABCDEF"
s = [(20, "A"), (20, "B"), (20, "C"), (10, "D"), (20, "E"), (10, "F")]
huffman(s, t)
