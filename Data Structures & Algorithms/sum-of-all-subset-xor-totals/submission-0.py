class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def get_xor(arr):
            if len(arr) == 0:
                return 0
            xor = arr[0]
            for i in range(1, len(arr)):
                xor ^= arr[i]
            return xor

        res= []
        def dfs(i, path):
            if i == len(nums):
                res.append(get_xor(path))
                return
            
            path.append(nums[i])
            dfs(i+1, path)
            path.pop()
            dfs(i+1, path)

        dfs(0, [])
        return sum(res)