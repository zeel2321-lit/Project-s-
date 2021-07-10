# how to add items to our list
# most common thing that you can do with your list and most important

fruits=['grapes','apple']
fruits.append('mango')
print(fruits)
# apeend fun will always add your data in the last position
# in real applicaiton we dn know how much elements are there so inorder to add something we just use append method

fruit=[]
#here we have just created a list and can add elements according to our need
fruit.append("mango")
fruit.append("banana")
fruit.append("guava")
print(fruit)

# more methods to add data
fruit1=['mango','orange']
#in case if we want to arrange data in particular position then we use insert method
fruit1.insert(1,'grapes')
print(fruit1)

# some more methods to add data in our list
# insert method
# how to join)concatenate) two list
fruit2=['grapes','apple']
fruitts =fruit1+fruit2
#print(fruitts)
#extend method
print(fruit1)
print(fruit2)
fruit1.extend(fruit2)
# difference between append and extend method
# extend-----> it will directly join two list
# append------> it will make sub list of the list