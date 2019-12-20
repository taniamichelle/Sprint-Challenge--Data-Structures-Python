import time
from binary_search_tree import BinarySearchTree
import sys
sys.path.append('../queue_and_stack')

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

# print('names1: ', names_1)

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# print('names2: ', names_2)

duplicates = []


# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# make tree
# traverse tree
# if names_1 contains name from names_2:
# append name to "duplicates"
# class NameTree(object):
#     def __init__(self, names_1):
#         self.root = self.generate_tree_from_file(names_1)

#     def __str__(self):
#         return str(self.root)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
