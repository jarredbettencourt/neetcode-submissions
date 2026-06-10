class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n== 1:
            return 1
        i = 1
        while True:
            n -= i
            if n <= 0:
                return i - 1
            i += 1