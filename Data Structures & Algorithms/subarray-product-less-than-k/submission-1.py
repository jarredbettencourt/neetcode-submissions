class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n, res = len(nums), 0

        for i in range(n):
            curProd = 1
            for j in range(i, n):
                curProd *= nums[j]
                if curProd >= k:
                    break
                res += 1

        return res