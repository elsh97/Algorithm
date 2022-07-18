n = int(input())
count,i=0,1
while True:
    i+=1
    if '666' in str(i):
        count+=1
        if count==n:
            print(i)
            break