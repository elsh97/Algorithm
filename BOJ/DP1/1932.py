n = int(input())
tri = []
for _ in range(n):
    tri.append(list(map(int, input().split())))

for i in range(1,n):
    if i==1:
        tri[i][0]+=tri[0][0]
        tri[i][1]+=tri[0][0]
        continue

    for j in range(i+1):
        if j==0:
            tri[i][j]+=tri[i-1][0]
        elif j==i:
            tri[i][j]+=tri[i-1][-1]
        else:
            tri[i][j] += max(tri[i-1][j-1],tri[i-1][j])

print(max(tri[-1]))