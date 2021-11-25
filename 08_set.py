"""
@Author: Zeehan 
@Date: 2021-25-11 19:00:30
@Title : union in set 
"""
"""
Description:
     declare variable and use .union to create union  

Parameter:
      
Return:
"""
setn1 = {10,20,30,40,80}
setn2 = {100,30,80,40,60}
print("Original sets:")
print(setn1)
print(setn2)
r1 = setn1.difference(setn2)
print("Difference of setc1 - setc2:")
print(r1)
r2 = setn2.difference(setn1)
print("Difference of setc2 - setc1:")
print(r2)
