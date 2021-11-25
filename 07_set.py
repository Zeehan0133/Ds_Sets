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
a={1,2,3,4,5}
b={5,6,7,8,9}
c={9,10,11,12,13}
# print(a | b |c)
print("before union" ,(a) ,(b) ,(c))
i=a.union(b,c)
print("after union :" ,(i))
