class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix = [0] * (len(nums) + 1)
        prefix[1] = nums[0]
        for i in range(2, len(prefix)):
            prefix[i] = nums[i - 1] + prefix[i - 1]
        l, r = 0, len(nums) - 1
        res = float('inf')
        print(prefix)
        while prefix[r] >= target:
            for l in range(r):
                if (prefix[r] - prefix[l]) >= target: 
                    res = min(res, r - l)
                r -= 1
        return 0 if res == float('inf') else res