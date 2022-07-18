import math
n = int(input())
gears = list(map(int, input().split()))

f = gears[0]
gears=gears[1:]
for g in gears:
    gcd = math.gcd(f,g)
    lcm = gcd*(f//gcd)*(g//gcd)
    print('{}/{}'.format(lcm//g, lcm//f))