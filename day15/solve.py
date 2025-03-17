def going(n):
    awal = 1
    res = 1

    for i in range(n, 1, -1):
        awal /= i
        res += awal

    return res
