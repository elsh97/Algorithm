from collections import deque
from sys import stdin

n = int(input())
Q = deque()
for i in range(n):
    cmd = stdin.readline().split()
    if len(cmd)==1:
        if cmd[0]=='pop':
            if 0<len(Q):
                print(Q.popleft())
            else:
                print(-1)
        
        elif cmd[0]=='size':
            print(len(Q))
       
        elif cmd[0]=='empty':
            if len(Q)==0:
                print(1)
            else:
                print(0)
        
        elif cmd[0]=='front':
            if len(Q)==0:
                print(-1)
            else:
                print(Q[0])

        elif cmd[0]=='back':
            if len(Q)==0:
                print(-1)
            else:
                print(Q[-1])
        
        else:
            pass

    elif len(cmd)==2:
        if cmd[0]=='push':
            Q.append(int(cmd[1]))
        else:
            pass
    else:
        pass