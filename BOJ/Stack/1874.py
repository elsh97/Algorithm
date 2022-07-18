from sys import stdin
from collections import deque

n = int(stdin.readline())

target = deque()
for _ in range(n):
    target.append(int(stdin.readline()))

s = deque()
flag=False
answer =''
for i in range(1, n+1):
    s.append(i)
    answer+='+\n'

    while 0<len(s) and target[0]==s[-1]:
        s.pop()
        target.popleft()
        answer += '-\n'

if len(target)==0:
    print(answer[:-1])
else :
    print('NO')    