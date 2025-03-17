def luck_check(st):
    R = 0
    L = len(st)
    r_sum = 0
    l_sum = 0

    while R < L:
        r_sum += int(st[R])
        l_sum += int(st[L - 1])
        R += 1
        L -= 1

    return r_sum == l_sum
