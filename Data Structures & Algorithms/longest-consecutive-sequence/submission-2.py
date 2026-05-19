class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        count = 0
        num_set = set(nums)
        for n in nums:
            if n - 1 not in num_set:
                m = n
                count = 1
                while m + 1 in num_set:
                    count += 1
                    m += 1
            res = max(res, count)
        return res