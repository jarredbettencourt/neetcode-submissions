class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[0:k], nums[k:] = nums[k:], nums[0:k]