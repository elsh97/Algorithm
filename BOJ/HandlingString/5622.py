dial = list(range(3,11))
a = dict()
for i in range(65,91):
    if i<80:
        a[chr(i)]=dial[(i-65)//3]
    elif 80<=i and i<84 :
        a[chr(i)] = dial[5]
    elif 84<=i<87:
        a[chr(i)] = dial[6]
    else:
        a[chr(i)] = dial[7]

time=0 
s=input().upper()
for c in s:
    time+=a[c]
print(time)