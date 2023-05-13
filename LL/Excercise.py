class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None
       
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1
       
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next          

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1



    def remove_duplicates(self):
        if self.length == 0:
            return None
        else:
            m = set()
            prev = None
            temp = self.head
            while temp != None:
                if temp.value in m:
                    temp = temp.next
                    prev.next  =  temp
                else:
                    m.add(temp.value)
                    prev = temp
                    temp = temp.next
                    
                
            
            
            
        
   



my_linked_list = LinkedList(1)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(3)
my_linked_list.append(2)
my_linked_list.append(4)
my_linked_list.remove_duplicates()

my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    1
    2
    3
    4
   
"""
