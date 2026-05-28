class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # res = float('inf')
        # memo = [-1] * (amount + 1)
        # def dfs(amount):
        #     res = float('inf')
        #     if amount == 0:
        #         return 0
        #     if memo[amount] != -1:
        #         return memo[amount]
            
        #     for coin in coins:
        #         if amount - coin >= 0:
        #             res = min(res, 1 + dfs(amount - coin))
        #     memo[amount] = res
        #     return res
        # res = dfs(amount)
        dp = [0] * (amount + 1)
        for i in range(amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = dp[i-c] + 1 
        return dp[amount] if dp[amount] != 1 else -1

        # return res if res != float('inf') else -1