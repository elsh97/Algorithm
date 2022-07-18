while True:
    x,y = map(int, input().split())
    if x==y==0:
        break

    if y%x==0:
        print('factor')
    elif x%y==0:
        print('multiple')
    else:
        print('neither')