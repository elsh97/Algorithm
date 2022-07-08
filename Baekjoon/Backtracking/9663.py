n=int(input())
count = 0
row = [-1]*n

def is_promising(x):
    for i in range(x):
        if row[x]==row[i] or abs(row[x]-row[i])==abs(x-i):
            return False
    return True

def nQueen(x):
    global count
    if x==n:
        count+=1
    
    else:
        for i in range(n):
            row[x]=i
            if is_promising(x):
                nQueen(x+1)

nQueen(0)
print(count)