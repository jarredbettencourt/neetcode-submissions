class Solution:
    def check(self, nums: List[int]) -> bool:
        down = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                down += 1
        return down == 0 or (down == 1 and nums[-1] <= nums[0])