class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        num_value = -1
        while nums:
            value = heapq.heappop(nums)
            if value - num_value > 1:
                return value - 1
            num_value = value
        return num_value + 1