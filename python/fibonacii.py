arr=[0,1]
def fibonacci(a):
  if a<=0:
    return "Enter valid index"
  elif a<=len(arr):
    return arr[a-1]
  else:
    b=fibonacci(a-1)+fibonacci(a-2)
    arr.append(b)
    return b


print(fibonacci(10))