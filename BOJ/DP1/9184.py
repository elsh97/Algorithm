w=[[[0]*21 for _ in range(21)] for _ in range(21)]
for x in range(21):
    for y in range(21):
        for z in range(21):
            if x<=0 or y<=0 or z<=0:
                w[x][y][z]=1
            elif x<y<z:
                w[x][y][z] = w[x][y][z-1]+w[x][y-1][z-1]-w[x][y-1][z]
            else:
                w[x][y][z] = w[x-1][y][z]+w[x-1][y-1][z]+w[x-1][y][z-1]-w[x-1][y-1][z-1]

while True:
    a,b,c = map(int, input().split())
    if a==b==c==-1:
        break
    if a<=0 or b<=0 or c<=0:
        print('w({}, {}, {}) = 1'.format(a,b,c))
        continue
    elif 20<a or 20<b or 20<c:
        print('w({}, {}, {}) = {}'.format(a,b,c,w[20][20][20]))
    else:
        print('w({}, {}, {}) = {}'.format(a,b,c,w[a][b][c]))