# function practice
def lchar(name):
    return name[-1]
# to print last index
print(lchar("janani"))

# fun to check num is odd or even
def odd_even(num):
    if num % 2 == 0:
        return " even"
    else:
        return "odd"
print(odd_even(5))

# or we can write like this'
#   def odd_even(num):
    #if num % 2 == 0:
      #  return " even"
       # return "odd"

def is_even(num):
    if num % 2==0:
        return True
    else:
        return False
print(is_even(9))

# python way to define fun
 
def even(n):
     return n %2==0
print(even(2))

# parameter ----> n 
# argument ---> 2
def ssong():
    return "happy birthday song"
print(ssong())