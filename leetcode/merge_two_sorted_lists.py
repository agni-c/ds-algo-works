# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        """
        the trick is to compare each element
        using 2 pointers l1,l2 
        which ever is bigger put the dummy node upon that
        """
        cur = dummy = ListNode() # pointer (in python assignment doesn't copy, it points to org memory location)
        
        # while we exust one list

        while l1 and l2 :
            if l1.val < l2.val:
                cur.next = l1
                l1= l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        if l1: cur.next = l1
        else: cur.next = l2
        
        return dummy.next