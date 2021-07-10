# functions
name =" janani"
 # for counting length of the string we use len() function
print(len(name))
# to define our own function 
# fun to add two num 
def add_two(a,b):   # ---> to define fun
    return a +b
total = add_two(10,4)
print(total)
print(add_two(5,4))

num1 =int(input("ENter 1st num:"))
num2 = int(input("Enter 2nd num: "))
t = add_two(num1,num2)
print(t)

# fun to concatenate two strings

fname=input("ENter 1st name:")
lname =input("Enter last name: ")
print(add_two(fname,lname))