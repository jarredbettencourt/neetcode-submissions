class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        i = 0
        j = 0
        while True:
            if s[i] >= g[j]:
                res += 1
                i += 1
                j += 1
            else:
                i += 1
            if i >= len(s) or j >= len(g):
                break
        return res
