from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    paren = list(stdin.readline().rstrip())
    rc =0 
    for p in reversed(paren):
        if p==')':
            rc+=1
        else :
            rc -=1
        if rc<0:
            break
    if 0==rc:
        print("YES")
    else:
        print("NO")