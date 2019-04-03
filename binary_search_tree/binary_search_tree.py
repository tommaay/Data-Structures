class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        new_node = BinarySearchTree(value)
        if value < self.value:
            if not self.left:
                self.left = new_node
            else:
                self.left.insert(value)

        elif value >= self.value:
            if not self.right:
                self.right = new_node
            else:
                self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left == None:
                return False
            return self.left.contains(target)
        elif target > self.value:
            if self.right == None:
                return False
            return self.right.contains(target)

    def get_max(self):
        target = self
        max_value = None
        while target:
            max_value = target.value
            target = target.right
        return max_value

    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    def __str__(self):
        return str(self.value)
