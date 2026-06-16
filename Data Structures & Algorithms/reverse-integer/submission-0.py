class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        res = 0
        if x < 0:
            negative = True
            x = -x
        while x != 0:
            n = x % 10
            res += n
            x //= 10
            res *= 10
        if res > (2**31 - 1):
            return 0
        return -(res // 10) if negative else res // 10