class Solution:
    def getSum(self, a: int, b: int) -> int:
        # xor a and b, get carry with a & b, shift to left, set b to carry, and repeat 
        while b:
            tmp = (a & b) << 1
            a = a ^ b
            b = tmp
        return a