class Node :
    def __init__(self, value):
        self.__value = value
        self.__next_node = None
    
    def __value(self):
        return self.__value

    def __next_node(self):
        return self.__next_node

    def get_value(self):
        return self.__value
    
    def set_value(self, value):
        self.__value=value

    def get_next_node(self):
        return self.__next_node
    
    def set_next_node(self, next_node):
        self.__next_node=next_node


head = Node('head')

for i in range(10):
    new_node = Node(i)
    if i==0:
        head.set_next_node(new_node)
    else:
        pointer = head
        while(pointer.get_next_node()!=None):
            pointer=pointer.get_next_node()
        pointer.set_next_node(new_node)

pointer = head
while(True):
    if pointer.get_next_node() == None:
        print("This value : {}  /  This is END of list".format(pointer.get_value()))
        break
    print("This value : {}  /  Next Value {}".format(pointer.get_value(), pointer.get_next_node().get_value()))
    pointer = pointer.get_next_node()