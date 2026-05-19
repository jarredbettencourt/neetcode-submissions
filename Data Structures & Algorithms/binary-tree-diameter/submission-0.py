# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # bottom up, assign each node to the sum of the max(length(root.left, root.right))
        res = 0
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            res = max(res, left_height + right_height)
            return 1 + max(left_height, right_height)
        dfs(root)
        return res
