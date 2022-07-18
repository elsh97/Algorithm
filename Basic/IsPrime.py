def is_prime(n):
    arr=[True]*(n+1)
    arr[0], arr[1] = False, False

    for i in range(2, int(n**0.5+1)):
        if arr[i]:
            j=2
        
        while i*j <= n:
            arr[i*j] = False
            j+=1
    return arr