class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Checking first if input is larger that parent
        # node and #self.right is vacant.
        # If so, call BST recursivley for right side.
        if value > self.value and not self.right:
            self.right = BinarySearchTree(value)
        # Do the same for the left side.
        if value < self.value and not self.left:
            self.left = BinarySearchTree(value)
        # If left and right are occupied, check if input value
        # is greater than the parent and insert left or right accordingly
        if value > self.value:
            self.right.insert(value)
        if value < self.value:
            self.left.insert(value)

    def contains(self, target):
        # Check value of searched input against self.value
        if self.value == target:
            return True
        # If no leaf nodes, return false
        elif not self.left and not self.right:
            return False
        # If searched input is greater than self.value...
        # call .contains() method on the right side.
        elif target > self.value:
            return self.right.contains(target)
        # If searched input is less than self.value...
        # call .contains() on left side.
        elif target < self.value:
            return self.left.contains(target)

    def get_max(self):
        maximum = -999999
        if self.value > maximum:
            maximum = self.value
        elif not self.right:
            return maximum
        while self.right:
            return self.right.get_max()
        return maximum

    def for_each(self, cb):
        pass
