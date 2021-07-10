# define greatest
#max of three num
def  greater(a,b,c):
    if a >b and a > c:
        return a
    else:
        if b > a and b > c:
            return b
        else:
            return c
n1 = int(input("Enter 1st num"))
n2 = int(input("Enter 2nd num"))
n3 = int(input("Enter 3rd num"))
big = greater(n1,n2,n3)
print(f"{big} is greatest")

# function inside function
# greatest (a,b)----> a or b
# greatest ((a or b , c ------> greatest))