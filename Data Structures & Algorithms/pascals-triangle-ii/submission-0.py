class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [int(digit) for digit in str(11 ** rowIndex)]