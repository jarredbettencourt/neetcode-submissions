class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        res = money - sum(prices[:2])
        return res if res >= 0 else money