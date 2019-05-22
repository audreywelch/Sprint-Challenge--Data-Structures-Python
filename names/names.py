import time

start_time = time.time()

f = open('/Users/audreywelch/Dropbox/Lambda School/Computer_Science/Sprint_03_Data-Structures/Sprint_Challenge_3/Sprint-Challenge--Data-Structures-Python/names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('/Users/audreywelch/Dropbox/Lambda School/Computer_Science/Sprint_03_Data-Structures/Sprint_Challenge_3/Sprint-Challenge--Data-Structures-Python/names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

## Runtime: O(n * m)

# duplicates = []
# for name_1 in names_1:                  # O(n)
#     for name_2 in names_2:              # O(m)
#         if name_1 == name_2:            
#             duplicates.append(name_1)   # O(1)

# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds") ## 12.1007 seconds

"""
PLAN:
-> Less Loops
    - "You might try importing a data structure you built during the week"
        .. Queue = this has a contains() method, so I would be traveling throughout a linked list, while checking if the value of the current node I'm at, is the value I'm looking for / a duplicate. Then update the `current` to be the next one in the list.
            >> Hmm, I'm pretty sure this would still be nested though.

"""

## Runtime: O(n + m)

dictionary = {}
duplicates = []

# Still iterating over n
for key in names_1:
    dictionary[key] = True # Setting a dummy value to be associated with the key

# Still iterating over m - but just checking if a key in the dictionary exists
for each_name in names_2:
    if each_name in dictionary:
        duplicates.append(each_name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime optimized approach: {end_time - start_time} seconds") ## 0.0099 seconds