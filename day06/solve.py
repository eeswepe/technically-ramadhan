def check(n):
    if n < 0:
        return 0
    elif n > 255:
        return 255
    else:
        return n


def rgb(r, g, b):
    # your code here :)
    red = hex(check(r))[2:]
    green = hex(check(g))[2:]
    blue = hex(check(b))[2:]
    return f"{red:0>2}{green:0>2}{blue:0>2}".upper()


print(rgb(0, 0, -20))
