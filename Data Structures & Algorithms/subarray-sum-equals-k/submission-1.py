class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # brute force
        res = 0
        for i in range(len(nums)):
            run_sum = 0
            for j in range(i, len(nums)):
                run_sum += nums[j]
                if run_sum == k:
                    res += 1

        return res