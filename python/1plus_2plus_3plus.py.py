# Exercise 4 chap 3
# problem
# ask user to input a number containing more than one digit
# ex  -1256
# calculate 1+2+5+6 and print
 
# algorithm  
# ask input in stirng , i.e don't chamge string to int 
# example "1256"
# pick string charcater one by one and change to int 
# int(example[0]) +int(example[1])+int(example[2]).... go upto len(example)

exam = (input("Enter number: "))
total =0
i=0
while i< len(exam):
    total += int(exam[i])
    i +=1
print(total)
