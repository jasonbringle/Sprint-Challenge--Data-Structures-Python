import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

#MVP
#For every name in the first list
# for name_1 in names_1:
    # Check if the name is in the second list
#     if name_1 in names_2:
    #Add it to the duplicates array
#         duplicates.append(name_1)

# Stretch
#Assign the two data arrays to two sets
set_names1 = set(names_1)
set_names2 = set(names_2)
#Make duplicates array append the difference between the two arrays by using the intersection method
duplicates = set_names1.intersection(set_names2)



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
