n,k = map(int, input().split())

s, p = 1, 1
if n-k<k:
    for i in range(k+1, n+1):
        p*=i
    for i in range(2, n-k+1):
        s*=i
else:
    for i in range(n-k+1, n+1):
        p*=i
    for i in range(2, k+1):
        s*=i
print((p//s)%10007)