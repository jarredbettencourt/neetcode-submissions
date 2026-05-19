class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            s1, s2 = -1 * heapq.heappop(stones), -1 * heapq.heappop(stones)
            if s1 == s2:
                continue
            elif s1 > s2:
                heapq.heappush(stones, -(s1 - s2))
            elif s2 > s1:
                heapq.heappush(stones, -(s2 - s1))
        return 0 if not stones else abs(stones[0])