class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # if amount == 0:
        #     return 0
        # dp = [0] * len(coins)


        # return dp[-1] if dp[-1] != 0 else -1
        res = float('inf')
        def dfs(i, path, path_sum):
            if i == len(coins) or path_sum < 0:
                return
            if path_sum == 0:
                nonlocal res
                res = min(len(path), res)
                return
 
            path.append(coins[i])
            dfs(i, path, path_sum - coins[i])
            path.pop()
            dfs(i + 1, path, path_sum)

        dfs(0, [], amount)
        return res if res < float('inf') else -1