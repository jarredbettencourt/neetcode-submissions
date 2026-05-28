class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # push all 1s to left except for 1
        ones = 0
        zeros = 0
        for c in s:
            if c == '1':
                ones += 1
            else:
                zeros += 1
        res = ""
        for _ in range(ones - 1):
            res += '1'
        for _ in range(zeros):
            res += '0'
        
        return res + '1'