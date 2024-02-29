t = int(input())


for _ in range(t):
    n = int(input())
    a = list(map(int, list(input())))



    presum = 0
    check = {}
    check[0] = 1
    ans = 0

    for idx in range(len(a)):
        presum += a[idx]
        ans += check.get(presum - (idx+1), 0)
        check[presum - (idx+1)] = 1 + check.get(presum - (idx+1) , 0)
    
    print(ans)