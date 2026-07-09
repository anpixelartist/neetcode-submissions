# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        f  =  head
        s = head

        while f and f.next:
            f = f.next.next
            s = s.next

        curr = s.next
        s.next = None
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            

        p2 = prev
        p1 = head

        while p1 and p2:
            temp1 = p1.next
            p1.next = p2
            temp2 = p2.next
            p2.next = temp1
            p1 = temp1
            p2 = temp2



        