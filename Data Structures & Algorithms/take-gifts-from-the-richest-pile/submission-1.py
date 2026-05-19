class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heapq.heapify_max(gifts)
        while k != 0:
            val = heapq.heappop_max(gifts)
            heapq.heappush_max(gifts, floor(sqrt(val)))
            k -= 1
        return sum(gifts)