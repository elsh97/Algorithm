from sys import stdin
from collections import deque

n,k = map(int, stdin.readline().split())
circle = deque([i for i in range(1,n+1)])

answer = '<'
while 1<len(circle):
    for _ in range(k-1):
        circle.append(circle.popleft())
    answer += (str(circle.popleft())+', ')
answer += (str(circle.popleft()) + '>')
print(answer)