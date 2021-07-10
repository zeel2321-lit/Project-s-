# list inside list
matrix =[[1,2,3],[4,5,6],[7,8,9]] #---> 2D lisy
# 3 items---> 3 list
print(matrix[0])
print(matrix[2])
for i in matrix:
    print(i)
for sublist in matrix:
    for j in sublist:
        print(j)

# how can we acces its value
print(matrix[1][1])
print(matrix[2][0])

# type function
s="string"
print(type(s))
print(type(matrix))