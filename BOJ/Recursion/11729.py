import sys
sys.setrecursionlimit(10**4)

def Hanoi(n,s,t,d):
    if n==1:
        print(s, d)
        return
    else:
        Hanoi(n-1,s,d,t)
        print(s, d)
        Hanoi(n-1,t,s,d)

n=int(input())
print((2**n)-1)
Hanoi(n,1,2,3)