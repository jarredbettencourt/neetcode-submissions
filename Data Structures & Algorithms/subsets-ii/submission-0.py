class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        visit = set()
        res = []


        def dfs(idx, path):
            if idx == len(nums):
                if tuple(sorted(path)) not in visit:
                    res.append(path[:])
                    visit.add(tuple(sorted(path[:])))
                return
            
            path.append(nums[idx])
            dfs(idx + 1, path)
            path.pop()
            dfs(idx + 1, path)


        dfs(0, [])
        return res