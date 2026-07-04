class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[j] % 2 == 0 and nums[i] % 2 == 1:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums