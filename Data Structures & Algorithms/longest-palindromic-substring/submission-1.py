class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return 1
    
        res = 0
        def get_palindrome_length(i, j):
            l, r = i, j
            while l >= 0 and r <= len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l:r]

        res = []
        for i in range(len(s) - 1):
            res.append(get_palindrome_length(i, i))
            res.append(get_palindrome_length(i, i + 1))
            
    
        return max(res, key=len)[1:]
