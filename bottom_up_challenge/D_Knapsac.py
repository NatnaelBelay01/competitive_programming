n, W = map(int, input().split())
weights = []
values = []
for _ in range(n):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)


dp = [[0 for _ in range(len(values) + 1)] for _ in range(W + 1)]


for r in range(W + 1):
    for c in range(1, n + 1):
        pick = 0
        if r - weights[c - 1] >= 0:
            pick = dp[r - weights[c - 1]][c - 1] + values[c - 1]
        dp[r][c] = max(pick, dp[r][c - 1])

print(dp[-1][-1])
