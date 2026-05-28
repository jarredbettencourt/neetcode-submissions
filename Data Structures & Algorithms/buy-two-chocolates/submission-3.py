class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # prices.sort()
        # res = money - sum(prices[:2])
        # return res if res >= 0 else money

        heapq.heapify(prices)
        sum_choc = heapq.heappop(prices) + heapq.heappop(prices)
        res = money - sum_choc
        return res if res >=0 else money