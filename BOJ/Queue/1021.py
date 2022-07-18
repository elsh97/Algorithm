from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
target = list(map(int, stdin.readline().split()))

deq = deque([i for i in range(1,n+1)])

count = 0
for t in target:
    while deq[0]!=t:
        if deq.index(t)<=len(deq)-deq.index(t):
            deq.append(deq.popleft())
            count+=1
        else : 
            deq.appendleft(deq.pop())
            count+=1
    deq.popleft()
print(count)