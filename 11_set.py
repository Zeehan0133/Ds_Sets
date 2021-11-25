"""
@Author: Zeehan 
@Date: 2021-25-11 19:00:30
@Title : frozen set program 
"""
"""
Description:
          firstly we declare one set and then converted in frozen set and print it 

Parameter:
      
Return:
"""
from typing import FrozenSet


snum={9,9,8 ,1 ,0 ,7 ,3 ,8,6,3 }
print(snum,type(snum))
# converting set to frozenset
fnum = frozenset(snum)
print(type(fnum))
# printing details
print("frozenset set is : ", fnum)

