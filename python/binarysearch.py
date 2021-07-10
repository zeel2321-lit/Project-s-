
#BINARY SEARCH

def binarysearch(arr,l,r,x):
    if l<=r:                #base case/condition
        mid = int((l+r)/2)
        if(arr[mid]==x):  #element is found
            return mid
        elif arr[mid]>x: #element on left side
            return binarysearch(arr,l,mid-1,x)
        else:           #element on right side
            return binarysearch(arr,mid+1,r,x)
    else:
        return -1


arr = [2,3,4,5,6,7,8,9,10]
key = 9  #the element to be searched
status = binarysearch(arr,0,len(arr)-1,key)#Array,li,ri
# 0--> left index 
#len(arr)-1----> right index
if(status == -1):
    print("Element not found")
    
else:
    print("Element found at index",status)