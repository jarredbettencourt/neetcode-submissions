class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        last = nums[0]
        res = nums[0]
        cur_sum = nums[0]
        for n in nums[1:]:
            if n > last:
                cur_sum += n
            else:
                cur_sum = n
            last = n
            res = max(res, cur_sum)
        return res 