def ks(val, W, wt, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]
                              + K[i-1][w-wt[i-1]],
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][W]


n = int(input("Enter the number of values: "))
value = list(map(int, input("Enter profits: ").split()))
wt = list(map(int, input("Enter weights: ").split()))
sum = int(input("Enter the max weight u want: "))
print(ks(value, sum, wt, n))