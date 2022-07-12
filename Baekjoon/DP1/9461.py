a = int(input())
for _ in range(a):
    n = int(input())
    tri = [1,1,1,2,2]
    for i in range(5,n):
        tri.append(tri[i-5]+tri[i-1])
    print(tri[n-1])