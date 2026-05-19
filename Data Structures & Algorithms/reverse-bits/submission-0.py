class Solution:
    def reverseBits(self, n: int) -> int:
        temp = 0
        i = 0
        while n > 0:
            popped_bit = n & 1
            temp = temp << 1 
            temp = temp | popped_bit
            n = n >> 1
            i += 1
        for _ in range(32 - i):
            temp = temp << 1
        return temp