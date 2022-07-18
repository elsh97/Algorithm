from sys import stdin

line=''
while True:
    line = stdin.readline().rstrip()
    if line=='.':
        break
    
    paren=[]
    flag = False
    for c in line:
        if not (c=='(' or c==')' or c=='[' or c==']'):
            continue
        elif c=='(' or c=='[':
            paren.append(c)
        else:
            if len(paren)==0:
                flag=True
                break
            elif c==')' and paren[-1] !='(':
                flag=True
                break
            elif c==']' and paren[-1] !='[':
                flag=True
                break
            else:
                paren.pop()
    if not flag and len(paren)==0:
        print('yes')
    else :
        print('no')