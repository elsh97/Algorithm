x,y,w,h = map(int, input().split())
m = min(x,y,w-x,h-y)
if m==x:
    print(x)
elif m==y:
    print(y)
elif m==w-x:
    print(w-x)
else:
    print(h-y)