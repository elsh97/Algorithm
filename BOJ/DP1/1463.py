from sys import stdin
input = stdin.readline

n = int(input())
dp = [0]*(10**6+1)

dp[1]=0
dp[2]=1
dp[3]=1
for i in range (4, n+1):
    a,b,c = 1e99,1e99,1e99
    if i%2==0:
        a = dp[i//2]+1
    if i%3==0:
        b = dp[i//3]+1
    c = dp[i-1]+1
    dp[i]=min(a,b,c)

print(dp[n])