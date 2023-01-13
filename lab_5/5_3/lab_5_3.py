kod = {"A": "", "B": "", "C": "", "D": "", "E": "", "F": "", "G": "", "H": "", "I": "", "J": "", "K": "", "L": "",
       "M": "", "N": "", "O": "", "P": "", "R": "", "S": "", "T": "", "U": "", "W": "", "Y": "", "Z": ""}


def shannon_fano(symbols):
    if len(symbols) > 1:
        symbols = sorted(symbols, reverse=True)
        left = []
        sum_left = 0
        right = symbols
        sum_right = 0
        for symbol in right:
            sum_right += symbol[0]
        i = 0
        while i < len(symbols):
            if abs((sum_left + right[0][0]) - (sum_right - right[0][0])) < abs(sum_left - sum_right):
                s = right.pop(0)
                left.append(s)
                sum_left += s[0]
                sum_right -= s[0]
                i += 1
            else:
                break
        for symbol in left:
            kod[symbol[1]] += "0"
        for symbol in right:
            kod[symbol[1]] += "1"
        shannon_fano(left)
        shannon_fano(right)


text = "AGCDJF"
symbols = [(20, "A"), (20, "G"), (20, "C"), (10, "D"), (20, "J"), (10, "F")]

shannon_fano(symbols)
for entry in kod:
    if kod[entry] != "":
        print(f"{entry} {kod[entry]}")
print(f"Text: {text} -> ", end="")
for litera in text:
    print(kod[litera], end="")
