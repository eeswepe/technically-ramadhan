def alt_or(lst):
    if len(lst) == 0:
        return None
    ret = lst[0]
    for i in range(1, len(lst)):
        if lst[i] != lst[i - 1]:
            ret = True
    return ret
