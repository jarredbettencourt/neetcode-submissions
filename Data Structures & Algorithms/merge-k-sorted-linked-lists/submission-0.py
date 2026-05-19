# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Scan through lists repeatedly, and pick lowest node
        # When lowest node is picked, create new node with it, and add to list
        # Set lowest node to next
        # Stop when all nodes are None
        dummy = ListNode(0)
        num_lists = len(lists)
        # all_nodes_exhausted = False
        lowest_idx = -1 
        cur = dummy
        while True:
            lowest_value = float('inf')
            for i in range(num_lists):
                if not lists[i]:
                    continue
                if lists[i] and lowest_value > lists[i].val:
                    lowest_value = lists[i].val
                    lowest_idx = i
            if lowest_value == float('inf'):
                break
            cur.next = lists[lowest_idx]
            lists[lowest_idx] = lists[lowest_idx].next
            cur = cur.next
        return dummy.next