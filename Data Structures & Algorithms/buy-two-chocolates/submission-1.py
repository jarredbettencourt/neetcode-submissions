class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # prices.sort()
        # res = money - sum(prices[:2])
        # return res if res >= 0 else money

        choc = [float('inf')] * 2
        for p in prices:
            if p < choc[0] and p < choc[1]:
                choc[0] = p
            elif p < choc[1] and p >= choc[0]:
                choc[1] = p
        res = money - sum(choc)
        return res if res >=0 else money