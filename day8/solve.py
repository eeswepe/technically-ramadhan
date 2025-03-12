def increment_string(strng):
    if len(strng) == 0:
        return "1"

    if strng.isdigit():
        return str(int(strng) + 1).zfill(len(strng))

    marker = len(strng)

    for i in range(len(strng) - 1, -1, -1):
        if not strng[i].isdigit():
            marker = i + 1
            break

    angka = strng[marker:]
    if angka == "":
        return strng + "1"

    if marker == 0:
        return str(int(angka) + 1).zfill(len(angka))

    return strng[:marker] + str(int(angka) + 1).zfill(len(angka))


print(increment_string("foo"))
