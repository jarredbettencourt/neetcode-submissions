# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def recurse(root, targetSum):
            if not root:
                return False
            if root and not root.left and not root.right and targetSum - root.val == 0:
                return True
            if root and not root.left and not root.right and targetSum - root.val != 0:
                print('hi')
                return False
            return recurse(root.left, targetSum - root.val) or recurse(root.right, targetSum - root.val)
        return recurse(root, targetSum)