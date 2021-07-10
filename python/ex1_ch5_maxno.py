# Exercise 1 chap 5
# max num
def  greater(a,b):
    if a >b:
            return a
    else:
            return b
n1 = int(input("Enter 1st num"))
n2 = int(input("Enter 2nd num"))
big = greater(n1,n2)
print(f"{big} is greater")