# Exercise 3
# take the coma seperated input from user
# a single character
 #output - 2 print lines
  # 1. user's name length
   # 2. count the character that user inputed ( bonus : case insensitive count)

name,char = input("Enter your name and Enter the single character : ").split(",")

print(len(name))
print(f"character count : {name.lower().count(char.lower())}")
