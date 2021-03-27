class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numlen = len(nums)
        left=  [1]*numlen 
        right= [1]*numlen 
        result=[1]*numlen 
        pointingVal = 1
        
        #left to right
        for i in range(numlen):
            left[i]=pointingVal
            pointingVal *= nums[i]
        print(left)
         
        #right to left
        pointingVal=1
        for i in range(numlen-1,-1,-1):
            right[i]=pointingVal
            pointingVal *= nums[i]
        print(right)
        
        #result
        for i in range(numlen):
            result[i]=left[i]*right[i]
        
        return result