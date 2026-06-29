class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res_increase_len = 1
        res_decrease_len = 1
        cur_increase_len = 1
        cur_decrease_len = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cur_increase_len += 1
                res_decrease_len = max(res_decrease_len, cur_decrease_len)
                cur_decrease_len = 1
            elif nums[i] < nums[i-1]:
                cur_decrease_len += 1
                res_increase_len = max(res_increase_len, cur_increase_len)
                cur_increase_len = 1
            else:
                res_decrease_len = max(res_decrease_len, cur_decrease_len) 
                res_increase_len = max(res_increase_len, cur_increase_len)
                cur_decrease_len = 1
                cur_increase_len = 1
        res_decrease_len = max(res_decrease_len, cur_decrease_len) 
        res_increase_len = max(res_increase_len, cur_increase_len)

        return max(res_increase_len, res_decrease_len)