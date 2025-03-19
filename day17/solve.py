dp = [0 for i in range(10000000)]
dp[0] = 1
dp[1] = 1


def fibo(n):
    global dp
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]


def perimeter(n):
    fibo(n + 1)
    return 4 * sum(dp[: n + 1])
