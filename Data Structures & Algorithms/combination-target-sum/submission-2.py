class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        visit = set()
        res = []
        nums.sort()
        def dfs(i, path, path_sum):
            if i == len(nums) or path_sum > target:
                return
            if path_sum == target:
                res.append(path.copy())
                return

            path.append(nums[i])
            dfs(i, path, path_sum + nums[i])
            path.pop()
            dfs(i + 1, path, path_sum)


        dfs(0, [], 0)
        return res