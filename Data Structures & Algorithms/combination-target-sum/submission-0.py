class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(idx, path):
            target_sum = sum(path)
            if target_sum == target:
                res.append(path)
                return
            elif target_sum > target or idx > len(nums) - 1:
                return

            path.append(nums[idx])
            backtrack(idx, path)

            path.pop()
            backtrack(idx + 1, path)

        for i in range(len(nums) - 1):
            backtrack(i, [])
        return res