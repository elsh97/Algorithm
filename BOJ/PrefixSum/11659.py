from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))

p = [0]*(n+1)
for i in range(1,n+1):
    p[i] = p[i-1]+num[i-1]

for _ in range(m):
    i, j = map(int, input().split())
    print(p[j]-p[i-1])