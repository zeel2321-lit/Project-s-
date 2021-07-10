#ask a user for name
# example - Zeel janani
# print count of each word
# output :
    # Z :1
    # e: 2
    # l:1
     # j :1
     # a : 2
     # n :2
     # i : 1

name = input("Enter yoour name :")

count =0
tmp = ""
i=0
while i < len(name):
    if name[i] not in tmp:
        tmp += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i = i+1
