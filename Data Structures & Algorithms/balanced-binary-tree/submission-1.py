# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def getHeight(root: Optional[TreeNode]) -> bool:
            if not root:
                return 1 
        
            leftHeight = 1 + getHeight(root.left)
            rightHeight = 1 + getHeight(root.right)
            return abs(leftHeight - rightHeight) <= 1

        return getHeight(root.left) and getHeight(root.right)