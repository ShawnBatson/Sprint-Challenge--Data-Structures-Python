"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
####### BELOW IS AN INSERT. FAR DOWN IS THE ASSIGNMENT ############


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):  # RECURSION NEEDED
        # compare to the new value we want to insert 8 root 3 insert
        if value < self.value:
            if self.left is not None:  # IF self.left is already taken by a node,
                self.left.insert(value)  # make that (left) node call insert.
            else:
                # set the left to the new node with the new value
                self.left = BSTNode(value)
        if value >= self.value:  # if new value is >= self.value
            if self.right is not None:  # IF self.right is taken by a node
                # make that (right) node call insert
                self.right.insert(value)
            else:
                # set the right child to the new node with new value.
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        if target >= self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree

    def get_max(self):
        # set the max value to a variable
        # move right from the first value, if there is no right, you are at the highest.
        max_value = self.value
        if self.right is None:
            return max_value
        else:
            max_value = self.right.get_max()
        return max_value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call it on the original value
        # check to see if the current node has a left attribute that isn't None
        if self.left is not None:
            # then call this function on the left value if there is one
            self.left.for_each(fn)
        fn(self.value)
        # check to see if the current node has a right attribute that isn't None
        if self.right is not None:
            # Then call this function on the right value if there is one
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):  # node will be the first object used, root structure
        # if the left attribute is not none (node.left)
        if node.left is not None:
            self.in_order_print(node.left)
        print(node.value)
        if node.right is not None:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):  # create a queue for nodes
        queue = []  # create a queue for nodes
        queue.append(node)  # add the first node to the queue
        # throw out a while loop:
        while len(queue) > 0:  # While queue is not empty
            current_node = queue.pop(0)  # remove the first node from the queue
            print(current_node.value)  # print the removed node
            # add all children to the queue (left and right)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []  # create the stack
        stack.append(node)  # append the first node
        while len(stack) > 0:  # while the stack exists
            # pull the last value in the stack
            current_node = stack.pop(len(stack)-1)
            print(current_node.value)  # print that value
            if current_node.right:  # if there is a right attribute
                stack.append(current_node.right)  # add this value to the stack
            if current_node.left:  # if there is a left attribute
                stack.append(current_node.left)  # add that to the stack.

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(self.value)  # print the first value
        if self.left is not None:
            # call the function on all left attributes down the line
            self.left.pre_order_dft(self.left)  # recursive
        if self.right is not None:
            # then call the function on all the right attributes
            self.right.pre_order_dft(self.right)  # recursive

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if self.left is not None:
            self.left.post_order_dft(self.left)  # call all left attributes
        if self.right is not None:
            self.right.post_order_dft(self.right)  # call all right attributes
        print(self.value)  # THEN print the value.
