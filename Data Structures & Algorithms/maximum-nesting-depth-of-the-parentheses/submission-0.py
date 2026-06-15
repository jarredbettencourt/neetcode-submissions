class Solution:
    def maxDepth(self, s: str) -> int:
        cur_depth = 0
        res = 0
        for char in s:
            if char == '(':
                cur_depth += 1
                res = max(cur_depth, res)
            elif char == ')':
                cur_depth -= 1
        return res