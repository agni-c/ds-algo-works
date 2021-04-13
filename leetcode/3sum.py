from typing import List

'''
To find the sum of 3 numbers most optimally
* loop over the array
* for every element find the two sum of it using two pointers
* left index will be i+1 and right index will be n-1
* upon facing duplicates just run loop which passes the duplicates
'''

def threeSum(self, nums: List[int]) -> List[List[int]]:
        result =[]
        nums.sort()
        
        for i,num in enumerate(nums):
            if i>0 and nums[i] == nums[i-1]: continue
                
            l,r=i+1,len(nums)-1
           
            while l < r :
                threesum = num + nums[l] + nums[r]
                if threesum == 0:
                    result.append([num , nums[l] , nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r: #only works when duplicates exists
                        l+=1
                elif threesum > 0:
                    r -=1
                else:
                    l += 1
        return result