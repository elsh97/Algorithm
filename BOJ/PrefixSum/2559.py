from sys import stdin
input = stdin.readline

n, k = map(int, input().split()) 
temp = list(map(int, input().split()))

ps = [0 for i in range(n+1)]
for i in range(1, n+1):
    ps[i] = ps[i-1]+temp[i-1]

dp = [0]*(n-k+1)
for i in range(n-k+1):
    dp[i] = ps[i+k]-ps[i]
print(max(dp))