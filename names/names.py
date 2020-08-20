
from binary_search_tree import BSTNode
import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Return the list of duplicates in this data structure
duplicates = []
# Replace the nested for loops below with your improvements

# MVP#############   1 second average

# for i in names_1:
#     if i in names_2:
#         duplicates.append(i)

###MVP 2 ##########################

# [duplicates.append(x) for x in names_1 if x in names_2]

#######Stretch########

bst = BSTNode(names_1[0])

for i in range(1, len(names_1)-1):
    bst.insert(names_1[i])

for name in names_2:
    if bst.contains(name):
        duplicates.append(name)

# .01 second


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
