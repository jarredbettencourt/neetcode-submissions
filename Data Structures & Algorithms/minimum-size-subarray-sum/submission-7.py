class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = nums[i] + prefix[i-1]
        # print(prefix)
        l, r = 0, len(nums) - 1
        res = float('inf')
        # while (nums[r] + nums[l]) >= target:
        #     res = min(res, r - l + 1)
        #     l += 1
        while r >= 0 or prefix[r] >= target:
            for l in range(r):
                if (prefix[r] - prefix[l]) >= target: 
                    res = min(res, r - l)
            r -= 1
        return 0 if res == float('inf') else res