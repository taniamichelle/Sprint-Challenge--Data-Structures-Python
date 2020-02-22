import time
from binary_search_tree import BinarySearchTree
import sys
sys.path.append('../queue_and_stack')

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


duplicates = []  # initialize empty array to hold duplicate names
# combine both names lists into single list of names
names = [names_1 + names_2]
# print('names: ', names)

# instantiate binary search tree instance from imported BinarySearchTree Class
name_tree = BinarySearchTree('Names')

# iterate through names list and insert names into name_tree
for name in names:
    if len(names) != 0:  # while names array is NOT empty:
        name_tree.insert(name)  # insert name into tree
        names[0].pop()  # remove name
    else:
        print('updated names list: ', names)

# traverse tree
name_tree.bft_print(self.name_tree)

# if there are duplicate names:

# append name to "duplicates"


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
