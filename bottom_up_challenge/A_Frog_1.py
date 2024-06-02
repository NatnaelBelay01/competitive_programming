n = int(input())

h = list(map(int, input().split()))
dp = [0] * len(h)

for i in range(len(h) - 1, -1, -1):
    a, b = float('inf'), float('inf')
    if i == len(h) - 1:
        continue
    if i < len(h) - 1:
        a = abs(h[i] - h[i + 1]) + dp[i + 1]
    if i < len(h) - 2:
        b = abs(h[i] - h[i + 2]) + dp[i + 2]
    dp[i] = min(a, b)

print(dp[0])
