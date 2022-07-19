from sys import stdin
input = stdin.readline

n = int(input())
num = list(map(int, input().split()))
dp = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if num[j]<num[i] and dp[i]<dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))