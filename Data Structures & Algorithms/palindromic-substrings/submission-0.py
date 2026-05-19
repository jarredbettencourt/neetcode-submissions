class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def countHelper(s, l, r):
            temp_res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                temp_res += 1
                l -= 1
                r += 1
            return temp_res

        for i in range(len(s)):
            res += countHelper(s, i, i) # odd length strings
            res += countHelper(s, i, i + 1)
        return res