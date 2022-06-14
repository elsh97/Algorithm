n=int(input())
bodies = []
for i in range(n):
    w,h = map(int, input().split())
    bodies.append([w,h,1])

for i in range(n):
    for j in range(n):
        if i==j:
            continue
        elif bodies[i][0] < bodies[j][0] and bodies[i][1]<bodies[j][1]:
            bodies[i][2]+=1
        else:
            continue

for i in range(n):
    if i==n-1:
        print(bodies[i][2])
    else:
        print(bodies[i][2], end=' ')
