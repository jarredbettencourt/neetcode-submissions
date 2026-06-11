class Solution:
    def countOdds(self, low: int, high: int) -> int:
        res = 0
        for i in range(low, high + 1):
            if i % 2:
                res +=1
        return res