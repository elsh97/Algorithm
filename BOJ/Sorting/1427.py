n = list(map(int, list(input())))
n.sort(reverse=True)
for i in n:
    print(i,end='')
print()