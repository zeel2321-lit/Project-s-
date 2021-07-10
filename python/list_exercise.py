# define a function which will take list containing numbers as input
# and return list containing square of every element
# example
# number =[1,2,3,4]
# square_list(number)----> return---->[1,2,9,16]
numbers=[1,2,3,4]
def square_list(l):
    square=[]
    for i in l:
        square.append(i*i)
    return square
print(square_list(numbers))


# exercise 2

# define a function which will take list as a argument
# and this fucntion will return a reversed list
# example--->
# [1,2,3,4]----> ['4,3,2,1]
# ['word1','word2']----> ['word2','word1']
# note
# for reverse method --->[::-1]

# num = list(range(1,6))
# using popO() and append() method 
# which is genrally used in real life application  , in websites
def reverse_list(l):
    rev =[]
    for j in range(1,len(l)+1):
        popped_item=l.pop()
        rev.append(popped_item)
    return rev
number = [1,2,3,4]
print(reverse_list(number))
        # rev.append(numbers.pop())
    # return rev
# print(reverse_list(num))

# with reversee method
def rev_list(l):
    # return l.reverse() ----> we can not write like this  cz it will change originla list 
    l.reverse()
    return l
number = [1,2,3,4]
print(rev_list(number))

def reverse_list(l):
    return l[::-1]
number = [1,2,3,4]
print(reverse_list(number))


# define a function that take list of words as arguement amd
# return list with reverse of every element in that list
# example
# ['abc','tuv','xyz']-----> ['cba','vut','zyx]

def rev_elements(l):
    elements =[]
    for i in l:
        elements.append(i[::-1])
    return elements
words=['abc','tuv','xyz']
print(rev_elements(words))

# Exercise 4
# filter odd even
# define a function
# input
# list----> [1,2,3,4,5,6,7]

def filter_odd_even(l):
    odd_nums=[]
    even_nums=[]
    for i in l:
        if i %2 == 0:
            even_nums.append(i)
        else:
            odd_nums.append(i)
    output =[odd_nums, even_nums]
    return output
nums= [1,2,3,4,5,6,7]
print(filter_odd_even(nums))

# exercise 5
# common elements ffinder function
# define a function which takes 2 list as input and return a list
# which contains common elements of the list
# example
# input ---> [1,2,5,8],[1,2,7,6]
# output----> [1,2]

def filter_similar(l1,l2):
    output=[]
    for i in l1:
        if i in l2:
            output.append(i)
    return output
print(filter_similar([1,2,5,8],[1,2,7,6]))

# min _max function
n =[6,60,2]
print(min(n))

print(max(n))

# define a fun which gives greates difference n which take list as an input
def greatest_diff(l):
    return max(l)-min(l)
print(greatest_diff(n))

# exercise 6
# define a function which takes input as a list
# [1,2,3,[1,2],[3,4]]----> input
# output---> 2--->no of list
# sublist counter
def nu(l):
    count = 0
    for i in l:
        if type(i)== list:
            count+=1
    return count
mix=  [1,2,3, [1,2], [3,4], ]
print(nu(mix))
