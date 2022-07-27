import sys
input = sys.stdin.readline

p = 1000000007
n, m = map(int, input().split())

"""
페르마의 소정리를 활용  (Fermat's Little Theorem)
if p is prime number, then
    (a**p) % p = a % p
so, 
    a**(p-2) % p = a**-1 % p
"""
def power(a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    elif b%2:
        return (power(a, b//2)**2 *a) %p
    else :
        return (power(a, b//2)**2) %p

facto = [1 for i in range(n+1)]
for i in range(2, n+1):
    facto[i] = i*facto[i-1]%p
numerator = facto[n]
denominator = facto[n-m] * facto[m] % p

print(numerator * power(denominator, p-2) % p)

"""
def comb(i,j):
    if i==2:
        if j==1:
            return 2
        else:
            return 1
    elif j==0 or i==j:
        return 1
    elif j==1 or j == i-1:
        return i
    return (comb(i-1,j-1)+comb(i-1, j))%1000000007
print(comb(n, m))

-> RecursionError -> Memory exceed
"""