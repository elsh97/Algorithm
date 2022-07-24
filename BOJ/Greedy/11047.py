from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
coin = [0]*n
for i in range(n):
    coin[i] = int(input())
coin.sort(reverse=True)

answer = 0
for c in coin:
    answer += k//c
    k = k-(k//c)*c

print(answer)