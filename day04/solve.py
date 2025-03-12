def count_score(s):
    sum = 0
    for i in s:
        sum += ord(i) - 96
    return sum


def high(s):
    str_list = s.split(" ")
    best_str = ""
    best_score = -999999
    for i in str_list:
        score = count_score(i)
        if score > best_score:
            best_score = score
            best_str = i
    return best_str


print(count_score("aa"))
print(count_score("b"))

print(high("aa b"))
