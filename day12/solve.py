def move_zeros(lst):
    for i in range(len(lst)):
        if lst[i] == 0:
            lst.append(0)
            lst.remove(0)
    return lst
