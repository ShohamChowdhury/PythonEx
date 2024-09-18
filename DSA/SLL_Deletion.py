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
                print(n.data, end="->")
                n = n.next
            print(None)

    def add_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node

    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_after(self, data, point):
        if self.head is None:
            print("Linked List is Empty")
            return

        n = self.head
        while n is not None:
            if n.data == point:
                break
            n = n.next

        if n is None:
            print("Error 404 : Node not Found")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def add_before(self, data, point):
        if self.head is None:
            print("Linked List is Empty")
            return

        if self.head.data == point:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return

        n = self.head
        while n.next is not None:
            if n.next.data == point:
                break
            n = n.next

        if n.next is None:
            print("Error 404 : Node not Found")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def delete_last(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        n = self.head
        while n.next.next is not None:
            n = n.next
        n.next = None

    def delete_first(self):
        if self.head is None:
            return
        self.head = self.head.next

    def delete(self, point):
        if self.head is None:
            print("Error Deletion : Empty LinkedList")
            return
        if self.head.data == point:
            self.head = self.head.next
            return
        n = self.head
        while n.next is not None:
            if n.next.data == point:
                n.next = n.next.next
                return
            n = n.next
        print("Error 404 : Node not Found")


LL1 = LinkedList()
LL1.add_first(30)
LL1.add_first(20)
LL1.add_last(50)
LL1.add_first(10)
LL1.add_before(40, 50)
LL1.add_after(60, 50)
LL1.print_LL()
print("deleting 50")
LL1.delete(50)
LL1.print_LL()
print("deleting first")
LL1.delete_first()
LL1.print_LL()
print("deleting last")
LL1.delete_last()
LL1.print_LL()
