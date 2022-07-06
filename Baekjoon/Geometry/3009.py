dix, diy = {}, {}
for _ in range(3):
    x,y=map(int, input().split())
    if x in dix:
        dix[x] += 1
    else:
        dix[x] = 1
    if y in diy :
        diy[y] += 1
    else:
        diy[y] = 1
x = [k for k,v in dix.items() if v==1]
y = [k for k,v in diy.items() if v==1]
print(x[0],y[0])