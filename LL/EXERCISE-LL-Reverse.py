class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
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
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1   
        return True  

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail= temp
        before = None    
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp  =  after
    
    def find_middle_node(self):
        fast = self.head
        slow = self.head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def has_loop(self):
        fast = self.head
        slow = self.head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
    
    def find_kth_from_end (ll, k):
        fast = ll.head
        slow = ll.head
        for i in range (k):
            if fast == None:
                return None
            fast = fast.next     
        while fast != None:
            slow = slow.next
            fast = fast.next
        return slow

    def reverse_between(self, m, n):
            if not self.head:
                return None
            
            dummy = Node(0)
            dummy.next = self.head
            prev = dummy
            
            for i in range(m):
                prev = prev.next
            
            current = prev.next
        
            for i in range(n - m):
                temp = current.next
                current.next = temp.next
                temp.next = prev.next
                prev.next = temp
        
            self.head = dummy.next
    
    
    def partition_list(self,x):
        if self.head == None:
            return None
        
        dum1 = Node(0)
        dum2 = Node(0)
        prev1 = dum1
        prev2 = dum2
        current = self.head
        while current:
            if current.value < x:
                prev1.next = current
                prev1 = current
            else:
                prev2.next = current
                prev2 = current
                current = current.next
                prev2.next = None
                prev1.next = dum2.next
                self.head = dum1.next

        
        
  



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

print('LL before reverse():')
my_linked_list.print_list()

my_linked_list.reverse()

print('\nLL after reverse():')
my_linked_list.print_list()
my_linked_list.find_middle_node()
my_linked_list.has_loop()
my_linked_list.find_kth_from_end(3)
my_linked_list.reverse_between()



"""
    EXPECTED OUTPUT:
    ----------------
    LL before reverse():
    1
    2
    3
    4

    LL after reverse():
    4
    3
    2
    1
    
"""