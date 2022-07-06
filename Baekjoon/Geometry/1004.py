def inCircle(a,b,x,y,r):
    if (a-x)**2+(b-y)**2<=r**2:
        return True
    else:
        return False

n = int(input())
for _ in range(n):
    x1,y1,x2,y2 = map(int, input().split())
    circles = int(input())
    count = 0
    for _ in range(circles):
        x,y,r=map(int, input().split())
        if inCircle(x1,y1,x,y,r) and inCircle(x2,y2,x,y,r):
            continue
        elif inCircle(x1,y1,x,y,r) or inCircle(x2,y2,x,y,r):
            count+=1
        else:
            continue
    print(count)
