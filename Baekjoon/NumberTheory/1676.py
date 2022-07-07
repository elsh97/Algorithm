n = int(input())
nn=1
for i in range(2, n+1):
    nn*=i
nn = list(str(nn))
for nnn in range(len(nn)-1, -1, -1):
    if nn[nnn]!='0':
        print(len(nn)-nnn-1)
        break