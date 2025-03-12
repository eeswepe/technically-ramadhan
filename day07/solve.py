def alphabet_position(text):
    ret = []
    text = text.lower()
    for char in text:
        if char.isalpha():
            ret.append(ord(char) - 96)
    return " ".join(map(str, ret))
