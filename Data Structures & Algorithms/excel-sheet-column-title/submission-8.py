class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            rem = (columnNumber - 1) % 26
            res.append(chr(rem + 65))
            columnNumber //= 26
        return "".join(res[::-1])