class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF  # 32 bit mask
    
        while b & mask:
            carry = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = carry
    
    # if result fits in 32 bits signed, return as is
    # if high bit is set, it's negative — convert back
        if a > 0x7FFFFFFF:  # greater than max positive 32 bit int
            a = ~(a ^ mask)  # two's complement conversion
    
        return a