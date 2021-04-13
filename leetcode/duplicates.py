class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict = {}
        for num in nums:
            if dict.get(num) == num :
                return True
            else:
                dict[num]=num
        return False

    def containsDuplicateOptmize(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums)==0: return False
        st = set()
        for num in nums: st.add(num)
        # expression returns true or false (set size < arr)
        return (len(st)<len(nums))  