class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0
        while l <= r:
            mid = (l + r) // 2
            product = mid * mid
            if product > x:
                r = mid - 1
            elif product < x:
                l = mid + 1
                res = mid
            else:
                return mid
        return res
# 0, 13
# 0, 5
# 3, 5
# 3, 4
# 