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

    def length(self):
        count = 0
        curr_node = self.head
        while curr_node is not None:
            count += 1
            curr_node = curr_node.next
        return count

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = new_node

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

    def add_after(self, value, x):
        curr_node = self.head
        while curr_node is not None:
            if curr_node.value == x:
                new_node = Node(value)
                new_node.next = curr_node.next
                curr_node.next = new_node
                break
            curr_node = curr_node.next
        else:
            print("Node isn't present")

    def add_before(self, value, x):
        new_node = Node(value)
        if self.head is None:
            print("Node isn't present")
            return
        if self.head.value == x:
            new_node.next = self.head
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            if curr_node.next.value == x:
                new_node.next = curr_node.next
                curr_node.next = new_node
                break
            curr_node = curr_node.next
        else:
            print("Node isn't present")

ll1 = LinkedList()
ll1.add(10)
ll1.add(25)
ll1.add(28)
ll1.add(29)
ll1.add(30)
ll1.add_after(20, 10)
ll1.add_before(45, 30)
ll1.show()
