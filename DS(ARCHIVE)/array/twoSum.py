from typing import List


class Solution:
    
    def _two_sum_brut_helper(self,arr, key) -> List[int]:
        ansArr = None
        
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
                       
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        return self._two_sum_brut_helper(nums,target)