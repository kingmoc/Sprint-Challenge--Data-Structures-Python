class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value: #main case
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        if value >= self.value: #main case #2
            if not self.right:
                self.right = BinarySearchTree(value) 
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # print('ran function')
        if target == self.value:
            # print('IS EQUAL', target, self.value)
            # return True
            return self.value

        if target < self.value:
            # print("less Than")
            if not self.left:
                # print('no left node')
                return False
                # return
            else:
                return self.left.contains(target)

        if target > self.value:
            # print("greater Than")
            if not self.right:
                # print('no right node')
                return False
                # return
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # print('ran function')
        if not self.right:
            # print('no right node', self.value)
            return self.value
        else:
            # print('right node exist')
            return self.right.get_max()
            
    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)

        if self.right:
            self.right.for_each(cb)