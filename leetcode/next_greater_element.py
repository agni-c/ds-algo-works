 def nextGreaterElementBrute(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums1:
            idx = nums2.index(i)
            for j in range(idx,len(nums2)):
                if nums2[j]> i:
                    res.append(nums2[j])
                    break
                elif j >= len(nums2)-1:
                    res.append(-1)
        return res

def nextGreaterElementStack(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        # value of the last ele alaways -1 (proparty) 
        stack = [nums2[-1]]
        table = {nums2[-1]:-1}
        
        for i in range(len(nums2)-2,-1,-1):
            
            while stack != [] and stack[-1] < nums2[i]:
                stack.pop()
            if len(stack)==0:
                table[nums2[i]] = -1
            elif stack[-1]> nums2[i]:
                table[nums2[i]] = stack[-1]
            stack.append(nums2[i])
             
        
        for i in nums1:
            res.append(table.get(i))
        
        return res


def nextGreaterElementStackMoreTweaks(self, find, nums):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    res = []
    stack = []
    table = {}
    
    for cur in reversed(nums):
        while stack and stack[-1]< cur:
            stack.pop()
        if len(stack)==0:
            table[cur]=-1
        elif stack[-1]> cur:
            table[cur]=stack[-1]
        stack.append(cur)      
            
    for i in find:
        res.append(table.get(i))
    
    return res