"""
@Author: Zeehan 
@Date: 2021-25-11 19:00:30
@Title : remove item from a set if it is present
"""
"""
Description: declare variable city and remove item with the of dis method
The built-in method, discard() in Python, removes the element from the set only 
if the element is present in the set.
If the element is not present in the set, 
then no error or exception is raised and the original set is printed
Parameter:
      
Return:
"""
num_set = set([0, 1, 2, 3, 4, 5])
print("Original set elements:")
print(num_set)
print("\nRemove 0 from the said set:")
num_set.discard(0)
print(num_set)
