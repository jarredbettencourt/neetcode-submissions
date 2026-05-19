class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)
        while k != 0:
            val = -heapq.heappop(gifts)
            heapq.heappush(gifts, -floor(sqrt(val)))
            k -= 1
        return -sum(gifts)