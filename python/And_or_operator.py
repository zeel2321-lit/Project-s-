# check two condition at same time
# and ,or
name = "zeel"
age = 19
if name =="zeel" and age==19:
    print ("true")
else:
    print("Flase")

if name =="zeel" or age==19:
    print ("true")
else:
    print("Flase")
 # Watch COCO
 # exercise 2
 # Ask user's name start with ("a" or "A") and age is above 10 then 
 # print---> you can watch coco movie
 # else part " sorry , tou cannot watch coco !"

name= input("Enter your name and : ")
age = int(input("Enter your age :"))
if (name[:1]=='a' or name[:1]=="A") and age >=10:
    print("you can watch coco movie")
else:
    print(" sorry , You cannot watch coco !")