# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head:
            slow = head
        else:
            return False    
        if head.next:
            fast = head.next
        else:
            return False

        while fast != slow :
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return False
            if fast == None:
                return False    

        return True        
