def add(a,b):
    c=a+b
    return c

def sub (a,b):
    c=a-b
    return c

def multiplication(a,b):
    c=a*b
    return c

def division(a,b):
    c=a/b
    return c

a=int(input("Enter 1st num :"))
b=int(input("ENter 2nd num:"))
choice=int(input("ENter 1 for addition \n Enter 2 for subtraction \n Enter 3 for multiplication \n Enter 4 for division \n "))
if(choice==1):
   c=add(a,b)
   print(c)
elif(choice==2):
   c=sub(a,b)
   print(c)
elif(choice==3):
   c=multiplication(a,b)
   print(c)
elif(choice==4):
   c=division(a,b)
   print(c)
else:
    print("Please enter propeer number ")