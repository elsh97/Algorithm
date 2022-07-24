from sys import stdin
input = stdin.readline

n = int(input())
d = list(map(int, input().split()))
g = list(map(int, input().split()))

cost, dist, answer = g[0], d[0], g[0]*d[0]
for i in range(1, n-1):
    if g[i]<cost:
        cost = g[i]
    answer = answer+cost*d[i]
print(int(answer))
