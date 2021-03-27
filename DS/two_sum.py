class Solution:
    
    def _two_sum_brut_helper(self,arr, key) -> List[int]:
        ansArr = None
        
       # iterate over every element
        for i in range(len(arr)):
            firstNum = arr[i]
            for j in range(i+1,len(arr)):
                secondNum = arr[j]
                sum = firstNum + secondNum
                if key == sum:
                    ansArr = [i,j] 
                    break
            if ansArr:
                break
                
        return ansArr
    
    def _two_sum_hash_helper(self,arr,key):
        nummap= {}

        for i,ele in enumerate(arr):
            if key - ele in nummap:
                return [nummap[key-ele],i]
            else:
                nummap[ele]= i
            
                    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        return self._two_sum_hash_helper(nums,target)