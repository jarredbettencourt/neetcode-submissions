class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            rem = columnNumber % 26
            res.append(chr(rem + 64))
            columnNumber //= 26
        return "".join(res[::-1])