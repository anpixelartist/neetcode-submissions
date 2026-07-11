# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        res = head
        carry = 0
        
        sum = 0

        while l1 or l2 or carry:
            if l1 and l2:
                sum = l1.val+l2.val+carry
            else:
                
                if l1:
                    sum = l1.val+carry
                elif l2:
                    sum = l2.val+carry
                else:
                    sum = carry    
                

            res.next = ListNode(sum%10)
            res = res.next
            carry = sum//10
            if l1:
                l1=l1.next
            if l2:    
                l2=l2.next
        return head.next    


        