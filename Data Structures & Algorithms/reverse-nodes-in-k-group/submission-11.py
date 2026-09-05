# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        GroupPrev = dummy

        while True:
            Kth = self.getKth(GroupPrev, k)
            if not Kth:
                break
            GroupNext = Kth.next

            curr, prev = GroupPrev.next, GroupNext
            while curr != GroupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = GroupPrev.next
            GroupPrev.next = Kth
            GroupPrev = tmp

        return dummy.next



    def getKth(self, curr: ListNode, k: int) -> Optional[ListNode]:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
