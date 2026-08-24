# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        if cur.next == None:
            return None
        ll_length = 0
        while cur:
            ll_length += 1
            cur = cur.next
        cur = head
        i = 0
        while cur:
            if i == ll_length - n - 1:
                cur.next = cur.next.next
                break
            cur = cur.next
            i += 1 

        return head

