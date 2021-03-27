# find the lowest value exist in all 3 array

def find_smallest(arr1,arr2,arr3):
    #init 3 pointers
    p1=p2=p3=0

    # Loop insures things doesn't get out of bound
    while(p1<len(arr1) or p2<len(arr2) or p3<len(arr3)):
        # condition to find the answer
        if arr1[p1]==arr2[p2]==arr3[p3]:
            return arr1[p1] #the values are same, can return either one

        #compare values in 3 arrays,move the lowest valued holding arr's pointer by 1
        elif p1<len(arr1) and arr1[p1]<arr2[p2] and arr1[p1]<arr3[p3]:
            p1 += 1
        elif p2<len(arr2) and arr2[p2]<arr3[p3] and arr2[p2]<arr1[p1]:
            p2 += 1
        elif p3<len(arr3) and arr3[p3]<arr1[p1] and arr3[p3]<arr2[p2]:
            p3 += 1

    return "Not Found"

   

