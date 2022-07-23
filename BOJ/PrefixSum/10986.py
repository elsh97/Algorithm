from sys import stdin
from collections import Counter
input = stdin.readline

n, m =map(int, input().split())
num = list(map(int, input().split()))
psum = [0]*(n+1)
for i in range(1, n+1):
    psum[i] = (psum[i-1]+num[i-1])%m

mod = Counter(psum)
mod[0] -= 1
answer = mod[0]
for i in range(n):
    answer += (mod[i]*(mod[i]-1))//2
print(answer)
