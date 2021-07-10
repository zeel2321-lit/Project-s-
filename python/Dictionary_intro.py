# dictionaries intro
# Que --> why we use dictionaries?
# Ans---> cz of limitations of lists , lists are not enough to represent real data

# example
user =['Zeel',20,['cool','kanii hii kem ch'],['awakening','fairy tale']]
# this list contains user name, age, fav movies, fav tunes, 
# you can do this but this is not a good way to do this

# Que---> what are dictionaries
# Ans---> unordered collection of data in key : value pair.

# how to create dicitonaries
user ={'name':"zeel","age":20}
print(user)
print(type(user))

# second method to create dictionary
user1 = dict(name ="zeel", age= 24)
print(user1)

# how to access data from dicionary
# Note There is no indexing because of unordered collection of data
# which type of data a dictionary can store
# ans---> Anything

# with the help of key we can acces data
print(user['name'])
print(user['age'])
dictA={'Name':'Zeel',
        'Student ID':'032',
        'Date of birth':'21',
        'Month of birth':'03',
        'Year of birth':'2001',
        'Name of the college':'Marwadi University',
        'SPI in sem 1':'8.95',
        'SPI in Sem 2':'7',
        'SPI in sem 3':'8.86',
        "Fav movies " : ["YJHD",'3 idiots','zindagi na milegi doobara']
        }
print(dictA)
print(dictA['Fav movies '])
# we can create dictionary inside dictionary
# user2{
   #  user3={

   #  }
# }
# how to add data in an empty dictionary
user2 ={}
user2['name'] = 'Zeel'
user2['age']='20'
print(user2)