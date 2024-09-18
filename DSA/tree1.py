class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.add_recursive(self.root, value)

    def add_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self.add_recursive(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self.add_recursive(current.right, value)

    def in_order_traversal(self, current, result):
        if current is not None:
            self.in_order_traversal(current.left, result)
            result.append(current.value)
            self.in_order_traversal(current.right, result)

    def get_in_order(self):
        result = []
        self.in_order_traversal(self.root, result)
        return result


tree = BST()
tree.add(10)
tree.add(5)
tree.add(12)
tree.add(11)
tree.add(13)
print(tree.get_in_order())
