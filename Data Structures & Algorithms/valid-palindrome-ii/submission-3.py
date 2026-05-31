class Solution:
    def validPalindrome(self, s: str) -> bool:
        res = 0
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                if s[l + 1] == s[r]:
                    res += 1
                    l += 2
                    r -= 1
                elif s[l] == s[r - 1]:
                    res += 1
                    r -= 2
                    l += 1
                else:
                    print(res)
                    return False
            else:
                l += 1
                r -= 1
        return res <= 1