# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # create ancestor list for p
        # create ancestor list for q
        # find last value that both lists share
        if not root:
            return None
        
        p_ancestors = []
        q_ancestors = []
        def find(root, target):
            cur = root
            ancestors = []
            while cur:
                ancestors.append(cur)
                if cur.val == target:
                    return ancestors
                elif cur.val > target:
                    cur = cur.left
                elif cur.val < target:
                    cur = cur.right

        p_ancestors = find(root, p.val)
        q_ancestors = find(root, q.val)
        iter_list = [p_ancestors, q_ancestors] if len(p_ancestors) > len(q_ancestors) else [q_ancestors, p_ancestors]
        for n in iter_list[0][::-1]:
            for m in iter_list[1][::-1]:
                if n.val == m.val:
                    return n  

        