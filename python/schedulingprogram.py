
def jobschedule(arr,t):
    n = len(arr)
    #sort in terms of desc order of marks
    for i in range(n):   #sorting as per desc order of marks
        for j in range(n-1-i):
            if(arr[j][2] < arr[j+1][2]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
                
    
    
    result = [False]*t  #indicative/status array
    job=['0']*t     #job sequence array
    for i in range(n):   #iterating through the job array 
        for j in range((arr[i][1]-1),-1,-1):  #through deadline
            if(result[j] is False):   #checking for empty slot
                result[j] = True
                job[j]=arr[i][0]
                break
            
    print(job)
            
    

arr = [["a",2,100],['b',1,19],['c',2,25],['d',2,25],['e',3,15]]
jobschedule(arr,3)  #homework--> to get the maximum deadline

