class Solution:
    def myPow(self, x: float, n: int) -> float:
        count = 1
        for _ in range(abs(n), 0, -1):
            count *= x
        return 1 / count if n < 0 else count 