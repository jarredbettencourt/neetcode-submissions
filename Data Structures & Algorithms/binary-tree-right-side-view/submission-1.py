# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # do bfs here, and then pick right most element
        if not root:
            return []
        q = deque([root])
        res = []

        while q:
            q_length = len(q)
            level = []
            for _ in range(q_length):
                e = q.popleft()
                level.append(e.val)
                if e.left: q.append(e.left)
                if e.right: q.append(e.right)
            if level:
                res.append(level[-1])
        return res