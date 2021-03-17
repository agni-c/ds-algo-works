# Rotated Arr search>> https://leetcode.com/problems/search-in-rotated-sorted-array/


from typing import List


class Solution:
    def _rotated_array_search_helper(self,arr,low,high,key):
        
        mid = (low + ((high - low) // 2))
    
        # normal checks
        if high <low:
            return -1
        if arr[mid] == key:
            return mid

        # sorted part
        # low -> mid range
        if arr[low] <= arr[mid] and key >= arr[low] and key <= arr[mid]:
            return self._rotated_array_search_helper(arr,low,mid-1,key)

        # mid -> high range
        elif arr[high] >= arr[mid] and key >= arr[mid] and key <= arr[high]:
            return self._rotated_array_search_helper(arr,mid+1,high,key)
        # rotated part
         # low -> mid
        elif arr[mid] >= arr[high]:
            return self._rotated_array_search_helper(arr,  mid + 1 , high , key)
        # mid -> high
        elif arr[low] >= arr[mid]:
            return self._rotated_array_search_helper(arr, low , mid - 1,  key)

        return -1

    # https://leetcode.com/problems/search-in-rotated-sorted-array-ii/   !!pending!!
    def _search_arr_helper_with_duplicate(self,arr,high,low,key):  
            
        #calc mid
        mid = low + ((high-low)//2)
        
        #checking condition
        if high<low:
            return False
        
        if arr[mid]==key:
            return True
        
        #conditon which checks for duplicate and srinks the search zone by 1
        if (arr[low]==arr[mid])and(arr[mid]==arr[high]):
            low += 1
            high -= 1
            return self._search_arr_helper_with_duplicate(arr,high,low,key)
            
        #non rotated arr conds
        #low -> mid
        elif arr[low]<=arr[mid] and arr[low]<=key and arr[mid]>=key:
            return self._search_arr_helper_with_duplicate(arr,mid-1,low,key)
        #mid-> high
        elif arr[mid]<=arr[high] and arr[mid]<=key and arr[high]>=arr[key]:
            return self._search_arr_helper_with_duplicate(arr,high,mid+1,key)
        
        #rotated part
        #low>mid
        elif arr[low]>=arr[mid]:
             return self._search_arr_helper_with_duplicate(arr,mid-1,low,key)
        #mid>high
        elif arr[mid]>=arr[high]:
            return self._search_arr_helper_with_duplicate(arr,high,mid+1,key)
        
        return False

        

    def search(self, nums: List[int], target: int) -> int:
        high = len(nums)-1
        return self._rotated_array_search_helper(nums , 0 , high , target)



sol =  Solution()

""""
[1,0,1,1,1]
3
[2,5,6,0,0,1,2]
3
[1,1,1,1,1,1,1,1,1,13,1,1,1,1,1,1,1,1,1,1,1,1]
13

"""


testArr1 = [4,5,6,7,0,1,2]
key = 0

result = sol.search(testArr1,key)
print(result)