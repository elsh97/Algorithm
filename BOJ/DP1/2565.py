from sys import stdin
input = stdin.readline

n = int(input())
line = [[] for _ in range(n)]
for i in range(n):
    line[i] = list(map(int, input().split()))
line.sort(key=lambda x:x[0])

# Using the method finding longest Increasing Sequence
dp = [0 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if line[j][1]<line[i][1] and dp[i]<dp[j]:
            dp[i]=dp[j]
    dp[i] += 1
print(n-max(dp))