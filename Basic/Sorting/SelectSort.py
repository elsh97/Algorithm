def solution(arr):
    for i in range(len(arr)):
        min_val = min(arr[i:])
        min_idx = arr.index(min_val)
        if arr[i]!=min_val:
            arr[i],arr[min_idx] = arr[min_idx],arr[i]
    return arr



test_set = [
    [3,45,6,1,2,5,76,7],
    [21,547,87,3,2,45,7,9],
    [1,2],
    [1,2,3,5],
    [8,24,6,32,4,7,42,5,147,1,35,3]
]

print("-"*10,"Select Sort","-"*10)
for i,arr in enumerate(test_set):
    print("#{} : {}".format(i, solution(arr)))

