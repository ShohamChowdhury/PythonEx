class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        n = self.head
        while n is not None:
            print(n.data, end="->")
            n = n.next
        print(None)

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = new_node
        new_node.prev = n

    def delete_last(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        if self.head.next is None:
            self.head = None
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.prev.next = None

    def delete_first(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def delete(self, value):
        if self.head is None:
            print("Linked List is Empty")
            return
        if self.head.data == value:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return
        n = self.head
        while n is not None:
            if n.data == value:
                break
            n = n.next
        if n is None:
            print("Node not found")
        else:
            n.prev.next = n.next
            if n.next is not None:
                n.next.prev = n.prev


# Example usage:
ll1 = LinkedList()
ll1.add(10)
ll1.add(20)
ll1.add(30)
ll1.add(40)
ll1.add(50)

ll1.print_ll()
ll1.delete(50)
ll1.print_ll()
