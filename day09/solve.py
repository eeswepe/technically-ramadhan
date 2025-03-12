def solution(roman: str) -> int:
    """complete the solution by transforming the roman numeral into an integer"""
    per_char = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    ret = 0
    for i in range(len(roman)):
        now = per_char[roman[i]]
        if i + 1 < len(roman):
            next = per_char[roman[i + 1]]
            if now < next:
                ret -= now
            else:
                ret += now
        else:
            ret += now

    return ret


while True:
    romawi_input = input("Masukkan angka romawi: ")
    print(solution(str(romawi_input)))
