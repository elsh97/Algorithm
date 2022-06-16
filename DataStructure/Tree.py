from pyrsistent import v


class Node :
    def __init__(self, value):
        self.__value = value
        self.__left_child_node = None
        self.__right_child_node = None

    def get_value(self):
        return self.__value
    
    def set_value(self, value):
        self.__value=value

    def get_left_child_node(self):
        return self.__left_child_node
    
    def set_left_child_node(self, left_child_node):
        self.__left_child_node = left_child_node

    def get_right_child_node(self):
        return self.__right_child_node
    
    def set_right_child_node(self, right_child_node):
        self.__right_child_node = right_child_node


node_arr = []
rand_arr = [2,4,6,1,28,64,23,7,9,42,11]
head = Node(-1)
node_arr.append(head)

for num in rand_arr:
    new_node = Node(num)
    node_arr.append(new_node)
    if head.get_left_child_node()==None and head.get_right_child_node()==None :
        head.set_left_child_node(new_node)
    elif head.get_right_child_node()==None:
        head.set_right_child_node(new_node)
    else:
        pointer=head
        while True:
            if pointer.get_value() > num and pointer.get_left_child_node()==None:
                pointer.set_left_child_node(new_node)
                break
            elif pointer.get_value() > num and pointer.get_left_child_node()!=None:
                pointer=pointer.get_left_child_node()
                continue
            elif pointer.get_value() < num and pointer.get_right_child_node()==None:
                pointer.set_right_child_node(new_node)
                break
            # elif pointer.get_value() < num and pointer.get_right_child_node()!=None:
            else:
                pointer=pointer.get_right_child_node()
                continue

for node in node_arr:
    l,r = "None", "None"
    v = node.get_value()
    if node.get_left_child_node() != None:
        l = node.get_left_child_node().get_value()
    if node.get_right_child_node() != None:
        r = node.get_right_child_node().get_value()

    if v==-1:
        print("[HEAD] value : {} / Left : {} / Right : {}".format(v,l,r))
    else:
        print("value : {} / Left : {} / Right : {}".format(v,l,r))
