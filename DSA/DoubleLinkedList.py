class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def show(self):
        elements = []
        if self.head is None:
            print("List is empty")
            return
        curr_node = self.head
        while curr_node is not None:
            elements.append(curr_node.value)
            curr_node = curr_node.next
        print(elements)

    def show_rev(self):
        elements = []
        if self.head is None:
            print("List is empty")
            return
        curr_node = self.tail  # Start from the tail
        while curr_node is not None:
            elements.append(curr_node.value)
            curr_node = curr_node.prev  # Traverse in reverse direction
        print(elements)

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def add_after(self, value, x):
        if self.head is None:
            print("List is empty")
            return
        new_node = Node(value)
        curr_node = self.head
        while curr_node is not None:
            if curr_node.value == x:
                new_node.prev = curr_node
                new_node.next = curr_node.next
                if curr_node.next is not None:
                    curr_node.next.prev = new_node
                curr_node.next = new_node
                if curr_node == self.tail:
                    self.tail = new_node
                break
            curr_node = curr_node.next
        else:
            print("Given node isn't present")

    def add_before(self, value, x):
        if self.head is None:
            print("The list is empty")
            return
        new_node = Node(value)
        curr_node = self.head
        while curr_node is not None:
            if curr_node.value == x:
                new_node.next = curr_node
                new_node.prev = curr_node.prev
                if curr_node.prev is not None:
                    curr_node.prev.next = new_node
                curr_node.prev = new_node
                if curr_node is self.head:
                    self.head = new_node
                break
            curr_node = curr_node.next
        else:
            print("Given node isn't present")

    def delete_begin(self):
        if self.head is None:
            print("The list is empty")
            return
        if self.head.next is None:
            self.head = None
            print("The list is empty")
        else:
            self.head = self.head.next
            self.head.prev = None
    def delete_end(self):
        if self.head is None:
            print("The list is empty")
            return
        if self.head.next is None:
            self.head = None
            print("The list is empty")
        else:
            self.tail.prev.next = None
            
    def delete(self,value):
        if self.head is None:
            print("Error : List is empty")
            return
        if self.head.next is None:
            if self.head.value == value:
                self.head = None
            else:
                print("Node is not found")
            return
        if self.head.value == value:
            self.head = self.head.next
            self.head.prev = None
            return
        if self.tail.value == value:
            self.tail.prev.next = None
            return
        curr_node = self.head
        while curr_node is not None:
            if curr_node.value == value:
                break
            curr_node = curr_node.next
        if curr_node is not None:
            curr_node.prev.next = curr_node.next
            curr_node.next.prev = curr_node.prev
        else:
            print("Can't find the Node")
                
DL = DoublyLL()
DL.add(10)
DL.add(12)
DL.add(16)
DL.add(7)
DL.add(8)
DL.show()
DL.delete(16)
DL.show()

