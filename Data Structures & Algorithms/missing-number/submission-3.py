class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums_sum = n * (n + 1) / 2 
        return int(nums_sum - sum(nums))