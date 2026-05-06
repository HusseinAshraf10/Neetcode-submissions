# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        D = ListNode()
        D.next = head
        l, r = D, head
        for _ in range(n):
            r = r.next
        while r:
            l, r = l.next, r.next
        temp = l.next
        l.next = temp.next
        temp.next = None
        return D.next
        