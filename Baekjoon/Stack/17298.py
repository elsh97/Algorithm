from sys import stdin
from collections import deque

n = int(stdin.readline())
answer = [-1]*n

s = deque()
arr = list(map(int, stdin.readline().split()))
for idx,i in enumerate(arr):
    if len(s)==0 or i<s[-1][1]:
        s.append([idx,i])
    else:
        while 0<len(s) and s[-1][1]<i:
            answer[s.pop()[0]] = i
        s.append([idx,i])    
for i in answer:
    print(i,end=' ')
print()