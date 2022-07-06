n = int(input())
d = []
idx_hm, idx_vm = -1,-1
for i in range(6):
    car, l = map(int, input().split())
    if car in [1,2]:
        if idx_hm==-1:
            idx_hm = i
        elif d[idx_hm]<l:
            idx_hm=i 
    else:
        if idx_vm==-1:
            idx_vm = i
        elif d[idx_vm]<l:
            idx_vm=i
    d.append(l)
minus_v = abs(d[(idx_hm-1)%6]-d[(idx_hm+1)%6])
minus_h = abs(d[(idx_vm-1)%6]-d[(idx_vm+1)%6])

print((d[idx_hm]*d[idx_vm]-minus_h*minus_v)*n)
            