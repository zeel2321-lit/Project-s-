
#method 1
def power(x,n):
    if(n==0):
        return 1
    elif(int(n%2)==0):
        return (power(x,int(n/2)) * power(x,int(n/2)))
    else:
        return (x * power(x,int(n/2)) * power(x,int(n/2)))
    
 
    
x = 2
n = 5 
print(power(x,n))
'''

'''
#method 2
def power(x,n):
    if(n==0):
        return 1
    elif(int(n%2)==0):
        return (power(x*x,int(n/2)))
    else:
        return (x * power(x*x ,int(n/2)))
    
     
x = 2
n = 5 
print(power(x,n))

#method 3
def power(x,n):
    if(n==0):
        return 1
    
    flag = power(x,int(n/2))
    if(int(n%2)==0):
        return (flag * flag)
    else:
        return (x * flag * flag)
    
     
x = 2
n = 5 
print(power(x,n))