class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber >= 1:
            rem = (columnNumber - 1) % 26
            res.append(chr(rem + 65))
            columnNumber //= 26
            # print(columnNumber)
        return "".join(res[::-1])