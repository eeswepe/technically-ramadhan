from collections import deque


def y(n):
    return 2 * n + 1


def z(n):
    return 3 * n + 1


def dbl_linear(n):
    arr = [1]
    hasil_y = deque([y(1)])
    hasil_x = deque([z(1)])

    for _ in range(n):
        if hasil_y[0] < hasil_x[0]:
            masuk = hasil_y.popleft()
        elif hasil_x[0] < hasil_y[0]:
            masuk = hasil_x.popleft()
        else:
            masuk = hasil_y.popleft()
            hasil_x.popleft()

        arr.append(masuk)
        hasil_y.append(y(masuk))
        hasil_x.append(z(masuk))

    return arr[n]


print(dbl_linear(20))
