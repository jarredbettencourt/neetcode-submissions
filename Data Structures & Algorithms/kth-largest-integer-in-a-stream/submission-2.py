import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.heap = nums
        self.k = k
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # self.stream.append(nums)
        heapq.heappush(self.heap, val)
        heapq.heappop(self.heap)
        return self.heap[0]