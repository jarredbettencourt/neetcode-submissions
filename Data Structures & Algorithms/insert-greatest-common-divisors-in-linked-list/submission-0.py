# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        # dummy = ListNode(0, head)
        # cur = dummy
        cur = head
        def get_gcd(a, b):
            start = min(a, b)
            for i in range(start, 0, -1):
                if a % i == 0 and b % i == 0:
                    return i
        while cur.next:
            next_node = cur.next
            gcd = get_gcd(next_node.val, cur.val)
            cur.next = ListNode(gcd, next_node)
            cur = next_node
        return head