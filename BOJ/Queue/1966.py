from sys import stdin
from collections import deque

test_count = int(stdin.readline())

for _ in range(test_count):
    n,m = map(int, stdin.readline().split())
    priorities = deque(map(int, stdin.readline().split()))
    flag, count = m,1
    
    while 0<len(priorities) :
        if priorities[0] == max(priorities):
            if flag == 0:
                print("count ",count)
                break
            priorities.popleft()
            flag -=1
            count+=1
        else:
            if flag==0:
                flag = len(priorities)
            priorities.append(priorities.popleft())
            flag -= 1