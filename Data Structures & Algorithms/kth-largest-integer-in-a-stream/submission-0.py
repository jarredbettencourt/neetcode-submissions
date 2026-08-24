import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.heap = nums
        self.k = k
        while len(self.heap) >= k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # self.stream.append(nums)
        print(self.heap)
        heapq.heappush(self.heap, val)
        num = heapq.heappop(self.heap)
        return num