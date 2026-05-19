class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr_size = 2 * len(nums)
        ans = [0] * arr_size
        for i in range(arr_size):
            ans[i] = nums[i % len(nums)]
        return ans