from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
stuff = [[] for _ in range(n)]
for i in range(n):
    stuff[i] = list(map(int, input().split()))

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(n):
    for j in range(1,k+1) :
        w,v = stuff[i][0], stuff[i][1]

        if j<w:
            dp[i][j] = dp[i-1][j]
        else :
            dp[i][j] = max(v+dp[i-1][j-w], dp[i-1][j])
# for i in range(n):
#     print(' '.join(map(str,dp[i])))
print(dp[n-1][k])