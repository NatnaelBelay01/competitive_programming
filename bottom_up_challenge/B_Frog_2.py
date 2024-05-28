n, k = map(int, input().split())

h = list(map(int, input().split()))


dp = [0] * len(h)

for i in range(len(h) - 1, -1, -1):
    if i == len(h) - 1:
        continue
    a = float('inf')
    for j in range(1, min(k + 1, len(h) - i)):
        temp = abs(h[i] - h[i + j]) + dp[i + j]
        a = min(a, temp)
    dp[i] = a
print(dp[0])

