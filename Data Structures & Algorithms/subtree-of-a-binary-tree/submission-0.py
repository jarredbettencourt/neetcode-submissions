# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        rootTraversal = ""
        def traverse(root):
            nonlocal rootTraversal
            if not root:
                return
            rootTraversal += str(root.val)
            traverse(root.left)
            traverse(root.right)

        traverse(root)
        rootTraversaltmp = rootTraversal
        rootTraversal = ""
        traverse(subRoot)
        subrootTraversaltmp = rootTraversal 
        # Return true if traversal of subroot is a substring of traversal of root
        print(subrootTraversaltmp)
        print(rootTraversaltmp)
        return subrootTraversaltmp in rootTraversaltmp