from sys import stdin
from collections import deque

n = int(stdin.readline())

target = deque()
for _ in range(n):
    target.append(int(stdin.readline()))
s = []

flag=False
answer =''
for i in range(1, n+1):
    s.append(i)

    answer+='+\n'

    while 0<len(target) and 0<len(s) and target[0]==s[-1]:
        s.pop()
        target.popleft()
        answer += '-\n'

        if 0<len(target) and 0<len(s) and target[0]<s[-1]:
            flag = True
            break
    
    if flag:
        print("no")
        break
if not flag:
    print(answer)