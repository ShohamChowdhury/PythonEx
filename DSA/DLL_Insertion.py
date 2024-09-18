class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Linked_List:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        n = self.head
        while n is not None:
            print(n.data, end="->")
            n = n.next
        print(None)

    def print_LL_rev(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        n = self.head
        while n.next is not None:
            n = n.next
        while n is not None:
            print(n.data, end="<-")
            n = n.prev
        print(None)

    def add_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = new_node
        new_node.prev = n

    def add_first(self, data):
        new_node = Node(data)
        if self.head is not None:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def add_after(self, data, value):
        if self.head is None:
            print("Linked List is Empty")
            return
        n = self.head
        while n is not None:
            if n.data == value:
                break
            n = n.next
        if n is None:
            print("Node not found")
        else:
            new_node = Node(data)
            if n.next is not None:
                n.next.prev = new_node
            new_node.next = n.next
            new_node.prev = n
            n.next = new_node

    def add_before(self, data, value):
        if self.head is None:
            print("Linked List is Empty")
            return
        if self.head.data == value:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            if n.next.data == value:
                break
            n = n.next
        if n.next is None:
            print("Node not Found")
        else:
            new_node = Node(data)
            new_node.next = n.next
            new_node.prev = n
            n.next.prev = new_node
            n.next = new_node


DLL = Linked_List()
DLL.add_last(20)
DLL.add_last(30)
DLL.add_last(40)
DLL.add_first(10)
DLL.add_after(15, 10)
DLL.add_before(35, 40)
DLL.add_before(25, 30)
DLL.print_LL()
DLL.print_LL_rev()
