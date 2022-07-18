def distance(x,y,a,b):
    return (x-a)**2+(y-b)**2

w,h,x,y,p = map(int, input().split())
count=0
r = (h/2)**2
for _ in range(p):
    a,b = map(int, input().split())
    if x<=a<=x+w and y<=b<=y+h:
        count+=1
    elif distance(x,y+h/2,a,b)<=r:
        count+=1
    elif distance(x+w, y+h/2, a,b)<=r:
        count+=1
    else:
        pass
print(count)