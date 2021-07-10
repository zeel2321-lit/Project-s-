# In keyword and iteraton in dictionary
user ={
    'name':'zeel',
    'age' : 20,
    "Fav movies " : ["YJHD",'3 idiots','zindagi na milegi doobara'],
    "fav_tunes" :['awakening','fairy tale']

}
# check if key exist in dicitonary
if 'name' in user:
    print("present")
else:
    print("not present")


# check if value exist in dictionary
if 'zeel' in user:
    print("present")
else:
    print("not present")
# it will not check the value it will only check key value
# so we use value() method
if 'zeel' in user.values():
    print("present")
else:
    print("not present")

# loops in dictionaries
for i in user:
    print(i)
# it will print all the keys of dicitonary

# it will print all the values of the dictionary
for i in user.values():
    print(i)
user_values = user.values()
# it will give output in list form
print(user_values)
print(type(user_values))

for i in user:
    print(user[i])

# items method is used when we want itterate any loop in dictionary
user_items =user.items()
print(user_items)
# [(),(),(),()]-----> tuple
print(type(user_items))

for key, value in user.items():
    print(f"key is {key} and value is {value}")

# tuple unpacking