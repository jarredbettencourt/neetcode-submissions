class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        count = {}
        for c in s:
            count[c] = 1 + count.get(c, 0)
            if count[c] % 2 == 0:
                res += 2
        for count in count.values():
            if count % 2 == 1:
                res += 1
                break
        return res