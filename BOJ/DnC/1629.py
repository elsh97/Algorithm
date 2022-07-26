from sys import stdin
input = stdin.readline

a,b,c = map(int, input().split())
def solution(a,b):
    if b==1:
        return a%c
    else :
        tmp = solution(a,b//2)
        if b%2==0:
            return tmp*tmp %c
        else:
            return tmp**2 * a %c
print(solution(a,b))