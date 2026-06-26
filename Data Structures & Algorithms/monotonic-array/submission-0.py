class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increase, decrease = False, False
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                increase = True
            elif nums[i] < nums[i-1]:
                decrease = True
        return increase ^ decrease