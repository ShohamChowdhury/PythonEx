class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next

    def add_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node

    def add_after(self, data, point):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                if n.data == point:
                    break
                n = n.next
            if n is None:
                print("The requested Node not found")
            else:
                new_node = Node(data)
                new_node.next = n.next
                n.next = new_node

    def add_before(self, data, point):
        if self.head is None:
            print("Linked List is Empty")
        elif self.head.data == point:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            n = self.head
            if n.data == point:
                LinkedList.add_begin(data)
            while n.next is not None:
                if n.next.data == point:
                    break
                n = n.next
            if n.next is None:
                print("Node not found")
            else:
                new_node = Node(data)
                new_node.next = n.next
                n.next = new_node


LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_after(20, 10)
LL1.add_after(40, 20)
LL1.add_last(50)
LL1.add_before(30, 10)
LL1.print_LL()
