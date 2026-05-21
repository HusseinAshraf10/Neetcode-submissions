# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.helper(lists, 0, len(lists) -1)

    def helper(self, lists,l, r):
        if l == r:
            return lists[l]
        mid = (l + r) // 2
        left = self.helper(lists,l, mid)
        right = self.helper(lists, mid + 1, r)
        return self.marge(left, right)

    def marge(self, a, b):
        D = ListNode()
        tail = D
        while a and b:
            if a.val <= b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next
        tail.next = a if a else b
        return D.next




