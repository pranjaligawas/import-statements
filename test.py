'''
#import ModuleName
import calc
print(calc.x)
calc.add(10,20)

#import ModuleName as alias
import calc as c
print(c.x)
c.add(10,20)

#from ModuleName import entity1,entity2,....
from calc import x,add
print(x)
add(10,20)
'''
#from ModuleName import *
from calc import *
print(x)
add(10,20)
