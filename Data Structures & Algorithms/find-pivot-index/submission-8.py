class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_array = [0] * len(nums)
        res = -1
        for i in range(1, len(nums)):
            prefix_array[i] = prefix_array[i-1] + nums[i-1]
        running_sum = 0
        for i in range(len(nums) - 1, -1, -1):
            if running_sum == prefix_array[i]:
                res = i
            running_sum += nums[i]
        return res