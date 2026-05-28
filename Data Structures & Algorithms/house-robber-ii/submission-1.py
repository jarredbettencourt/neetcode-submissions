class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        case_a = nums[1:]
        dp = [0] * len(case_a)
        dp[0] = case_a[0]
        dp[1] = max(case_a[0], case_a[1])
        for i in range(2, len(case_a)):
            dp[i] = max(dp[i-1], dp[i - 2] + case_a[i])
        case_a_res = dp[-1]

        case_b = nums[:-1]
        dp = [0] * len(case_b)
        dp[0] = case_b[0]
        dp[1] = max(case_b[0], case_b[1])
        for i in range(2, len(case_b)):
            dp[i] = max(dp[i-1], dp[i - 2] + case_b[i])
        case_b_res = dp[-1]
        return max(case_b_res, case_a_res)