n = int(input())
wines = [0] * 10001
for i in range(n):
    wines[i] = int(input())

dp = [0]*10001
dp[0] = wines[0]
dp[1] = wines[0] + wines[1]
dp[2] = max(wines[0]+wines[2], wines[1]+wines[2], dp[1])
for i in range(3, n):
    dp[i] = max(dp[i-3]+wines[i-1]+wines[i], dp[i-2]+wines[i], dp[i-1])

print(dp[n-1])
