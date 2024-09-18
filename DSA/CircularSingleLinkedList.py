class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    def show(self):
        elements = []
        curr_node = self.head
        if self.head is None:
            print("List is empty")
            return
        while True:
            elements.append(curr_node.value)
            curr_node = curr_node.next
            if curr_node == self.head:
                break
        print(elements)
    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        curr_node = self.head
        while curr_node.next != self.head:
            curr_node = curr_node.next
        curr_node.next = new_node
        new_node.next = self.head
    def add_begin(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            curr_node = self.head
            while curr_node.next != self.head:
                curr_node = curr_node.next
            curr_node.next = new_node
            self.head = new_node
    def add_end(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            curr_node = self.head
            while curr_node.next != self.head:
                curr_node = curr_node.next
            curr_node.next = new_node
            new_node.next = self.head
    def add_after(self,value,x):
        if self.head is None:
            print("List is empty")
            return
        new_node = Node(value)
        curr_node = self.head
        while curr_node.next != self.head:
            if curr_node.value == x:
                break
            curr_node = curr_node.next
        if curr_node.next is self.head:
            print("Node not found")
            return
        new_node.next = curr_node.next
        curr_node.next = new_node
    def add_before(self,value,x):
        if self.head is None:
            print("List is empty")
            return
        new_node = Node(value)
        curr_node = self.head
        if self.head.value is x:
            self.add_begin(value)
            return
        while curr_node.next != self.head:
            if curr_node.next.value == x:
                break
            curr_node = curr_node.next
        if curr_node.next is self.head:
            print("Node is not found")
            return
        new_node.next = curr_node.next
        curr_node.next = new_node
    def delete_begin(self):
        if self.head is None:
            print("The list is empty")
            return
        if self.head.next is self.head:
            self.head = None
            print("The list is now empty")
            return
        curr_node = self.head
        while curr_node.next is not self.head:
            curr_node = curr_node.next
        curr_node.next = self.head.next
        self.head = self.head.next
    def delete_end(self):
        if self.head is None:
            print("The list is empty")
            return
        if self.head.next is self.head:
            self.head = None
            print("The list is now empty")
            return
        curr_node = self.head
        while curr_node.next is not self.head:
            temp_node = curr_node
            curr_node = curr_node.next
        temp_node.next = self.head
    def delete(self,value):
        if self.head is None:
            print("The list is empty")
            return
        if self.head.next is self.head:
            if self.head.value == value:
                self.head = None
                print("The list is empty now")
                return
            print("The node isn't found")
        if self.head.value == value:
            self.delete_begin()
            return
        curr_node = self.head
        while curr_node.next is not self.head:
            if curr_node.next.value == value:
                break
            curr_node = curr_node.next
        if curr_node.next is self.head:
            print("The Node is not found")
        else:
            if curr_node.next.next is self.head:
                curr_node.next = self.head
                return
            curr_node.next = curr_node.next.next
                
CL = CircularLinkedList()
CL.add(5)
CL.add(8)
CL.add(10)
CL.add(12)
CL.add(15)
CL.add(16)
CL.add(19)
CL.show()
CL.add_after(9,12)
CL.show()