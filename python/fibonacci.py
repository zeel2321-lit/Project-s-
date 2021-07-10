# fibonacci series
 # 0 1 1 2 3 5 8 13 21 34
# how many num user want to print
# 1---> 0
# 2---> 0 1
# 3---> 0 1 1
 
# for i in range(1,11):
   #  print(i, end =" ,")
def fibo(n):
    a= 0
    b=1
    if  n ==1 :
        print(a)
    elif n==2:
        print(a,b) # a,b 0,1
    else:
        print(a,b ,end = " ")
        for i in range(n-2):
            c = a+b
            a=b
            b=c
            print(b ,end = " ")
fibo(10)