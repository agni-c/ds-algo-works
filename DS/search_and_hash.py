#binary_search

def binary_search(arr,low,high,key):
    
    # should be sorted
    if low <= high:
        
        #calculate the mid
        mid = low + ((high-low)//2)
        
        #key finding condition
        if arr[mid] == key:
            return mid
        
        if arr[mid]>key:
           return binary_search(arr,low,mid-1,key)
        else:
           return binary_search(arr,mid+1,high,key)
    else:
       
        return -1

testArr = [12,18,19,58,66,69,77,86,95,150]
key = 77
print(binary_search(testArr,0,len(testArr)-1,key))