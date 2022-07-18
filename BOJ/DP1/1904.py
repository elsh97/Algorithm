n = int(input())
tile = [0]*1000000
tile[0], tile[1] = 1, 2
for i in range(2, n):
    tile[i]=(tile[i-2]+tile[i-1])%15746
print(tile[n-1])

"""
In Python, variables doesn't have fixed size
Also Python doesn't support BigInt type
So without %(Modular) the result grows bigger and bigger, it consumes huge memory.

If I use 2 or 3 variables to solve this problem, then it would cost lot of time.
Since it has time complexity of n**2

So we have to save each result while constrain it's growth.
That's why we should do =% for each result before saving it in the array.
With this method, we can prevent huge memory usage and lower the time complexity at the level of n 
"""