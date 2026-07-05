class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        tmp = x
        res = 0
        while tmp:
            res *= 10
            res += (tmp % 10)
            tmp //= 10
        return res == x