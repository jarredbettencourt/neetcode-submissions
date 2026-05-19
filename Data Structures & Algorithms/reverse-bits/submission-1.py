class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            popped_bit = n & 1
            n = n >> 1
            res = res << 1
            res = res | popped_bit
        return res