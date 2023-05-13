class Node:
    def __init__(self, value):
        self.value = value
        self.first = None
        self.last = None
        

class BinarySearchTree:
    def __init__(self):
        self.root  = None


my_tree = BinarySearchTree()

print(my_tree.root)


 
"""
    EXPECTED OUTPUT:
    ----------------
    None

"""