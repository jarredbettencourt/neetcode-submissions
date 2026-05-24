class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while True:
            if columnNumber < 26:
                res.append(chr(columnNumber + 64))
                break
            else:
                res.append(chr(int(columnNumber / 26) + 64))
                columnNumber %= 26
        return "".join(res)