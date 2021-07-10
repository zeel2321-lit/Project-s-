# if else if statement
 # show ticket pricing for different age people
 # o to 3 (free)
 # 4 to 10 (150)
 # 11 to 60 (250)
 # above 60 (200)

age = int(input("Please enter your age :"))

if 0<age<=3:
     print("Ticket price: Free")
elif 3<age<=10:
       print(" TIcket price : 150")
elif 11<age<=60:
    print("Ticket price : 250")
elif age>60:
    print("Ticket price:: 60")
else: 
    print("you cannot watch")

a =float(input("Enetrr your num:"))

if 0<a<35:
    print("fail")
elif 50<a<=35:
    print("grade D")
elif 70<a<=50:
    print("Grade C")
elif 85<a<=70:
    print("Grade B")
elif 95<a<=85:
    print("Grade A")
elif a>=95:
    print("Grade O")
else:
    print("Please enter in proper format")