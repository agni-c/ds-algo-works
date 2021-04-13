# https://leetcode.com/problems/contains-duplicate/submissions/

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mydict = {}
        for num in nums:
            
            if mydict.get(num):
                return True
            else:
                mydict[num] = 1
           
        