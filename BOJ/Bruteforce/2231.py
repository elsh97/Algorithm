n = int(input())
for i in range(n):
    if i+sum([int(d) for d in str(i)]) == n:
        print(i)
        break
else:
    print(0)        
