def perimeter(n):
    a, b = 0, 1
    total = a + b
    for _ in range(1, n + 1):
        a, b = b, a + b
        total += b
    return 4 * total


print(perimeter(5))
