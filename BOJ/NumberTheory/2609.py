n = list(map(int, input().split()))
n.sort()
gcd, lcm = 0,0

for i in range(n[0], 0,-1):
    if n[0]%i==n[1]%i==0:
        gcd=i
        break
print(gcd)
lcm = (n[0]//gcd)*(n[1]//gcd)*gcd
print(lcm)