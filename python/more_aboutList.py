# more_aboutList.py
# generate lists with range function
from typing import no_type_check


numbers =list(range(1,11))
print(numbers)
#abc= list(range('a','j'))
# print(abc)

# something more about pop method
print(numbers.pop())
# it will return the value
popped_item= numbers.pop()
print(popped_item)
# index method
print(numbers.index(3))
# if we want to search particular items in the list
number=[1,2,3,4,5,6,1,10,11,5,1]
print(number.index(1,6))

def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative
number=[1,2,3,4,5,6,1,10,11,5,1]
print(negative_list(number))
# pass list to a funtion

