def cesar(text, s):
    result = ""
    for char in text:

        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)

        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    print(f"Text: {text} ->  {result}\n")


cesar("AbcDef", 3)
