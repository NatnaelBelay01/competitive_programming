n = int(input())

table = []
for _ in range(n):
    a, b, c = map(int, input().split())
    table.append([a, b, c])

dp = table[0][:]

for i in range(1, len(table)):
    temp = []
    for j in range(len(table[i])):
        ans = 0
        for k in range(len(dp)):
            if k != j:
                ans = max(ans, dp[k])
        temp.append(ans + table[i][j])
    dp = temp
print(max(dp))
