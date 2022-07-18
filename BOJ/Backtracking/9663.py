import time
start = time.time()
n = int(input())
row = [-1]*n
count=0

# def is_promising(x,row):
#     for i in range(x):
#         if row[i]==row[x] or abs(x-i)==abs(row[x]-row[i]):
#             return False
#     return True

def nQueen(x):
    global count
    if x==n:
        count+=1
        return
    
    # for i in range(n):
    #     row[x]=i
    #     if is_promising(x, row):
    #         nQueen(x+1)
    #     row[x]=-1

    for i in range(n):
        row[x]=i
        for j in range(x):
            if row[j]==row[x] or abs(x-j)==abs(row[x]-row[j]):
                break
        else:
            nQueen(x+1)
        row[x]=-1

nQueen(0)
print(count)
print(time.time()-start)