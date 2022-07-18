from sys import stdin

n,m = map(int, stdin.readline().rstrip('\n').split())
arr1 = list(stdin.readline().rstrip('\n'))
arr2 = list(stdin.readline().rstrip('\n'))
t = int(stdin.readline().rstrip())
answer=''

arr1 = [i for i in arr1[::-1]]
p = len(arr1)-t
if 0<p:
    answer += ''.join(arr1[:p])
    arr1 = arr1[p:]
    # print('--'*8)
    # print('answer: ',answer)
    # print('arr1: ',arr1)
    # print('arr2: ',arr2)
    # print('--'*8)
    while 0<len(arr1)+len(arr2):
        if len(arr2)==0:  pass
        else: answer+=arr2.pop(0)
        
        if len(arr1)==0:  pass
        else: answer+=arr1.pop(0)
        # print('--'*8)
        # print('answer: ',answer)
        # print('arr1: ',arr1)
        # print('arr2: ',arr2)
        # print('--'*8)

elif p<=0:
    p*=-1
    answer += ''.join(arr2[:p+1])
    arr2=arr2[p+1:]
    # print('--'*8)
    # print('answer: ',answer)
    # print('arr1: ',arr1)
    # print('arr2: ',arr2)
    # print('--'*8)
    while 0<len(arr1)+len(arr2):
        if len(arr1)==0:  pass
        else: answer+=arr1.pop(0)
        
        if len(arr2)==0:  pass
        else: answer+=arr2.pop(0)
        # print('--'*8)
        # print('answer: ',answer)
        # print('arr1: ',arr1)
        # print('arr2: ',arr2)
        # print('--'*8)
print(answer)