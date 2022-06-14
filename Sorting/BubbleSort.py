def solution(arr):
    len_arr = len(arr)
    for i in range(len_arr):
        for j in range(0,len_arr-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    
    return arr

test_set = [
    [3,45,6,1,2,5,76,7],
    [21,547,87,3,2,45,7,9],
    [1,2],
    [1,2,3,5],
    [8,24,6,32,4,7,42,5,147,1,35,3]
]

print("-"*10,"Bubble Sort","-"*10)
for i,arr in enumerate(test_set):
    print("#{} : {}".format(i, solution(arr)))

