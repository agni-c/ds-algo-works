class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums)<0: return max(nums)
        max_count=0
        local_count=0
        for num in nums:
            local_count+=num
            if local_count >max_count:
                max_count=local_count
            elif local_count <0:
                local_count =0 
                
        return max_count