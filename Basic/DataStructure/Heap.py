# Priority Queue can be made with HEAP
# Insertion : O(logn)
# Deletion : O(logn)

# Typically Heap is implemented in Array
# If,,, Parent Node's index : n
# Left Child Node's index : 2*n
# Right Child Node's index : 2*n+1

# Python has heapq library -> Default : min-heap
# heapq.heappush(heamp, item) -> Insert item
# heapq.heappop(heap) -> Delete smallest value, return the value
# heapq.heapify(list) -> turn list into heap

class MyMaxHeap:
    
    def __init__(self):
        self.arr = ['head']

    def push(self, item):
        self.arr.append(item)
        last_index = len(self.arr)-1
        while 0<last_index:
            parent_index = self.parent(last_index)
            if 0<parent_index and self.arr[parent_index]<self.arr[last_index]:
                self.arr[parent_index], self.arr[last_index] = self.arr[last_index], self.arr[parent_index]
                last_index = parent_index
            else:
                break

    def pop(self):
        last_index = len(self.arr)-1
        if last_index == 0 :
            return -1
        
        self.arr[1], self.arr[last_index] = self.arr[last_index], self.arr[1]
        max_value = self.arr.pop()
        self.heapify(1)
        return max_value

    def heapify(self, i):
        left_child = self.leftchild(i)
        right_child = self.rightchild(i)
        max_index = i

        if left_child <= len(self.arr)-1 and self.arr[i]<self.arr[left_child]:
            max_index = left_child
        if right_child <= len(self.arr)-1 and self.arr[max_index]<self.arr[right_child]:
            max_index = right_child
        
        if i!=max_index:
            self.arr[i], self.arr[max_index] = self.arr[max_index], self.arr[i]
            self.heapify(max_index)

    def printHeap(self):
        print(self.arr)
        print()

    def leftchild(self, index):
        return index*2
    
    def rightchild(self, index):
        return index*2+1

    def parent(self, index):
        return index//2
        

mh = MyMaxHeap()
test_arr = [2,45,6,8,4,3,68,5,7,11,1]
for i in test_arr:
    mh.push(i)
mh.printHeap()
print("pop!", mh.pop())
mh.printHeap()
print("pop!", mh.pop())
mh.printHeap()
print("pop!", mh.pop())
mh.printHeap()
print("pop!", mh.pop())