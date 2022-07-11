count_rec, count_dp = 0, 0


def fib(n):
    global count_rec
    if n==1 or n==2:
        count_rec+=1
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fibonacci(n):
    global count_dp
    f=[1,1]
    for i in range(2,n):
        f.append(f[i-2]+f[i-1])
        count_dp+=1
    return f[n-1]

n = int(input())
fib(n)
fibonacci(n)
print(count_rec, count_dp)
