def solution(arr):
    if len(arr)==1:
        return arr
    l_arr = solution(arr[:len(arr)//2])
    r_arr = solution(arr[len(arr)//2:])

    idx1,idx2=0,0
    new_arr=[]
    while idx1<len(l_arr) and idx2<len(r_arr):
        if l_arr[idx1] < r_arr[idx2]:
            new_arr.append(l_arr[idx1])
            idx1+=1
        else:
            new_arr.append(r_arr[idx2])
            idx2+=1
    
    new_arr += l_arr[idx1:]
    new_arr += r_arr[idx2:]

    return new_arr

test_set = [
    [3,45,6,1,2,5,76,7],
    [21,547,87,3,2,45,7,9],
    [1,2],
    [1,2,3,5],
    [8,24,6,32,4,7,42,5,147,1,35,3]
]

print("-"*10,"Merge Sort","-"*10)
for i,arr in enumerate(test_set):
    print("#{} : {}".format(i, solution(arr)))
