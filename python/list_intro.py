# list is a data structure
# list ----> this chapter
# it is a ordered collection of items

# you can store naything in list int, float, string

# we create list using square brackets

number =[1,2,3,4]
print(number[1])
words =["word1","word2","word3"]
print(words[2])
mixed =[1,2,3,4,"five","six",2.3,None]
print(mixed[:3])

# if we want to chnage the data in list

mixed[1:]='two'
print(mixed)
mixed[1:]=['two','four']
print(mixed)