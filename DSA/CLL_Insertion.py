class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class CircularLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def printll(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        n = self.head
        while True:
            print(n.data, end="->")
            n = n.next
            if n == self.head:
                break
        print(self.head.data)

    def printll_rev(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        n = self.tail
        while True:
            print(n.data, end="<-")
            n = n.prev
            if n == self.tail:
                break
        print(self.tail.data)

    def add_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.head.next = self.tail
            self.tail.prev = self.head
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        new_node.next = self.head
        self.head.prev = new_node
        self.tail = new_node

    def add_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.head.next = self.tail
            self.tail.prev = self.head
            return


cll = CircularLL()
cll.add_last(10)
cll.add_last(20)
cll.add_last(30)
cll.add_last(40)
cll.add_last(50)
cll.add_last(60)
cll.printll()
print("\n")
cll.printll_rev()
