from queue_and_stack import Queue
from queue_and_stack import Stack
from queue_and_stack import ListNode
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):  # we're just using 'value', no key
        self.value = value  # 'key'='value' since only using 'value'
        self.left = None  # left pointer
        self.right = None   # right pointer

    def __repr__(self):
        return(f'value = {self.value}, left: {self.left}, right: {self.right}')

    # Insert the given value into the tree
    def insert(self, value):
        '''
        adds the input value to the binary search tree, adhering to 
        the rules of the ordering of elements in a binary search tree.
        '''
        if self.value > value:  # if new value is < root's value:
            if self.left is None:  # if there's no root for left side:
                # new value becomes the left root
                self.left = BinarySearchTree(value)
            else:  # if there is a node for left side:
                # add new value as child of left parent node
                self.left.insert(value)

        if self.value <= value:  # if new value >= root's value:
            if self.right is None:  # if there's no root for the right side:
                # new value becomes the right root
                self.right = BinarySearchTree(value)
            else:  # if there is a root for the right side:
                # add new value as a child of right root
                self.right.insert(value)  # making recursive insert call

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        '''
        searches the binary search tree for the input value, returning a 
        boolean indicating whether the value exists in the tree or not.
        stops at first instance of the value.
        '''
        # search tree for input value
        # return boolean of True or False, depending on result
        if target == self.value:
            return True
        elif target < self.value:  # if target < self.value:
            if self.left is None:  # if there are no more left branches:
                return False    # return False
            else:
                return self.left.contains(target)  # go left (recursive)
        else:
            # if target > self.value:  <== don't need this line
            if self.right is None:
                return False
            else:
                # if self.right is not None:  <== don't need this line
                return self.right.contains(target)  # go right (recursive)

    # Return the maximum value found in the tree
    def get_max(self):
        '''
        returns the maximum value in the binary search tree.
        '''
        # look at values in branch right of root
        # if node has no right branch and is at rightmost branch, it's the max value
        # return value
        if self.right:  # if right exists:
            return self.right.get_max()  # call get_max() recursively
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach.
    def for_each(self, cb):
        '''
        performs a traversal of _every_ node in the tree, executing the 
        passed-in callback function on each tree node value. There is a myriad 
        of ways to perform tree traversal; in this case any of them should work
        '''
        cb(self.value)  # call cb on the value of each node
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)

        # -----------------------DEPTH-FIRST ITERATIVE SOLUTION:-----------------------
        # stack = Stack()  # use stack import from top
        # stack.push(self)  # pass in root node
        # while stack.len() > 0:  # keep running loop while there's something in stack
        #     current_node = stack.pop()
        #     if current_node.right:
        #         stack.push(current_node.right)
        #     if current_node.left:
        #         stack.push(current_node.left)
        #     cb(current_node.value)

    # ------------------------------ DAY 4 Project -------------------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node == None:  # if node == None:
            return  # return
        self.in_order_print(node.left)  # recursive call
        print(node.value)  # print node's value
        self.in_order_print(node.right)  # recursive call

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()  # Make a queue. references Queue class + gives us access to its methods
        q.enqueue(node)  # Pushing root into queue
        while q.len() != 0:  # While queue is not empty
            # removing old node (root) from queue
            current_node = q.dequeue()
            print(current_node.value)  # print value of current node
            if current_node.left:  # if left exists for our current node. add 'left' to back of q if there are pointers left
                # adding current node to queue. left continues moving the pointer left
                q.enqueue(current_node.left)
            if current_node.right:  # if right:
                q.enqueue(current_node.right)  # adding current node to queue

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        s = Stack()  # Make a stack
        s.push(node)  # put root in stack
        while s.len() != 0:  # while stack not empty
            current_node = s.pop()  # pop root out of stack
            print(current_node.value)  # print value of current node
            if current_node.left:  # if there are more left pointers
                s.push(current_node.left)  # add value of current node to stack
            if current_node.right:  # if there are more right pointers
                # add value of current node to stack
                s.push(current_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT. uncomment 94-97 in test.
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT. uncomment 99-102 in test.
    def post_order_dft(self, node):
        pass


tree = BinarySearchTree(5)
tree.insert(1)
# print(tree)
tree.insert(9)
tree.insert(8)
tree.insert(5)
tree.insert(2)

tree.bft_print(tree)
