# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 

        m = 0
        p = head
        while p:
            m += 1
            p = p.next

        r = m-n+1

        if r<2:
            head = head.next
            return head

        p = head    
        i  = 0
        
        while i<r-2:

            p = p.next
            i= i+1

        if n == m:
            p.next = None   
            
        else:
            p.next = p.next.next
             

        return head
