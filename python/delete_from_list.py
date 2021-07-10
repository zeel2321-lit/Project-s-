# common methods to delete data from list
fruits =['orange','apple','pear','banana','kiwi']
# pop method
fruits.pop()
print(fruits)
# here pop method will delete last element from the list when we dont pass any position/arguement
fruits.pop(1)
print(fruits)

# delete operator/statement
del fruits[1]
print(fruits)

# remove method
# when we don't know which element is in which position
fruits.remove('banana')
print(fruits)
fruits.remove('mango')
print(fruits)   # it will show error ---> not in list


# to add data in the list we use three methods
# --> append---> extend---> insert
# to remove data from the list we use three methods
# --> pop----> remove----> del