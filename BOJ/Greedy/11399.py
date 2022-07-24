from sys import stdin
input = stdin.readline

n = int(input())
t = list(map(int, input().split()))
t.sort()
dp = [0]*(n+1)
for i in range(1, n+1):
    dp[i] = dp[i-1]+t[i-1]
print(sum(dp)) 