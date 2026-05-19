# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ls = []
        cur = head
        while cur:
            ls.append(cur.val)
            cur = cur.next
        return ls == ls[::-1]