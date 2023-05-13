class Node:
    ## WRITE NODE CONSTRUCTOR HERE ##
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    
    def __init__(self, value):
        New_Node = Node(value)
        self.head  = New_Node
        self.tail = New_Node
        self.length = 1
        
my_linked_list = LinkedList(4)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)


"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    
"""

                                                                                                                    