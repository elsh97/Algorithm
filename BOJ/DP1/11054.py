from sys import stdin
input = stdin.readline

n = int(input())
num = list(map(int, input().split()))
dp1 = [0 for _ in range(n)]
dp2 = [0 for _ in range(n)]
answer = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if num[j]<num[i] and dp1[i]<dp1[j]:
            dp1[i]=dp1[j]
    dp1[i] += 1

for i in range(n-1,-1,-1):
    for j in range(n-1, i, -1):
        if num[j]<num[i] and dp2[i]<dp2[j]:
            dp2[i]=dp2[j]
    dp2[i]+=1

for i in range(n):
    answer[i] = dp1[i]+dp2[i]-1

# print(dp1)
# print(dp2)
# print(answer)
print(max(answer))