class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # res = float('inf')
        def dfs(amount):
            res = float('inf')
            if amount == 0:
                return 0
            
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            return res
        res = dfs(amount)


        return res if res != float('inf') else -1