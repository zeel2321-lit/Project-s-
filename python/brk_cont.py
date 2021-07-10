# break and continue keyword
# to print 1 to 10 num
for i in range(1,11):
    if i == 5:
        break
    print(i)

# continue

# print from 1 to 10 but not 5 , we can do this with continue

for i in range(1,11):
    if i ==5:
        continue   # we use continue to skip items
    print(i)