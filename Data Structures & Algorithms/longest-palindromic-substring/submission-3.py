class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        def getLongestPalindrome(i, j):
            sub = ""
            while i >= 0 and j < len(s) and s[i] == s[j]:
                sub = s[i:j+ 1]
                i-=1
                j+=1
            return sub

        for i in range(len(s)):
            odd_palindrome = getLongestPalindrome(i, i)
            even_palindrome = getLongestPalindrome(i, i+1)

            res = max(res, odd_palindrome, even_palindrome, key=len)
        return res

