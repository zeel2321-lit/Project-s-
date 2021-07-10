# split method
## convert string to list
from typing import AsyncContextManager


user_info='Zeel,2321'.split(',')
print(user_info)
name,age ='Zeel,2321'.split(',')
print(name)
print(age)



# join method
# convert list to string
user =['zeel','2321']
print(','.join(user))

# Accept the string from user of length not less than 10
# and conver that string to list of character and check
# if it is palindrome or not 

name=input("enter your name  : ")
if(len(name)>=10):
    word=name.split()
    #print(word)
    if word ==word[::1]:
        print("it is palinfrome")
    else:
        print("It is not palindrome")
else:
    print("Enter name properly whose length is more than 10")
    

