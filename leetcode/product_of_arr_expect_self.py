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


class Solution(object):
    def productExceptSelf(self, nums):
        output = [1] * len(nums)
        
        # multiply by the left side
        left_product = 1
        for i in range(1, len(nums)):
            left_product *= nums[i-1]
            output[i] = left_product
        
        # multiply by the right side
        right_product = 1
        for i in range(len(nums)-2, -1, -1):
            right_product *= nums[i+1]
            output[i] *= right_product
        
        return output