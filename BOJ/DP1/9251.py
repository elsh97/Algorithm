from sys import stdin
input = stdin.readline

w1 = list(input().rstrip())
w2 = list(input().rstrip())
dp = [0]*len(w2)

for i in range(len(w1)):
    count = 0
    for j in range(len(w2)):
        if count < dp[j]:
            count = dp[j]
        elif w1[i] == w2[j]:
            dp[j] = count+1

print(max(dp))
