class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def show(self):
        elements = []
        curr_node = self.head
        while curr_node is not None:
            elements.append(curr_node.value)
            curr_node = curr_node.next
        print(elements)
    
    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = new_node
             
    def length(self):
        count = 0
        curr_node = self.head
        while curr_node is not None:
            count+=1
            curr_node = curr_node.next
        return count
    
    def add_to_index(self, value, index):
        if index < 0 or index > self.length():
            print("Error: Index out of Range")
            return
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr_index = 0
            curr_node = self.head
            while curr_index < index - 1:
                curr_node = curr_node.next
                curr_index += 1
            new_node.next = curr_node.next
            curr_node.next = new_node
                
    def add_after(self,value,x):
        curr_node = self.head
        while curr_node is not None:
            if curr_node.value == x :
                new_node = Node(value)
                new_node.next = curr_node.next
                curr_node.next = new_node
                break
            curr_node = curr_node.next
            
    def add_before(self,value,x):
        new_node = Node(value)
        if self.head.value == x:
            new_node.next = self.head
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            if curr_node.next.value == x :
                new_node.next = curr_node.next
                curr_node.next = new_node
                break
            curr_node = curr_node.next
        else:
            print("Node isn't Present")    
            
    def delete_first(self):
        if self.head is None:
            print("The list is empty")      
            return
        self.head = self.head.next
    
    def delete_last(self):
        if self.head is None:
            print("The list is empty")
            return
        curr_node = self.head
        while curr_node.next.next is not None:
            curr_node = curr_node.next
        curr_node.next = None        
    
    def delete(self,value):
        if self.head is None:
            print("The list is empty")
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        curr_node = self.head
        while curr_node.next is not None:
            if curr_node.next.value == value:
                break
            curr_node = curr_node.next
        if curr_node.next is None:
            print("Error Deletion : Can't find the Node")
        else:
            curr_node.next = curr_node.next.next
                       
LL = LinkedList()
LL.add(15)
LL.add(11)
LL.add(17)
LL.add(16)
LL.add(18)
LL.show()
LL.delete_first()
LL.show()
LL.add(20)
LL.add(29)
LL.add(30)
LL.show()
LL.delete_last()
LL.show()
LL.delete(32)
LL.show()
        
