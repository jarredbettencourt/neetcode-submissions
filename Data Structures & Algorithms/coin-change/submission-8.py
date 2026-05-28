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
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-c]) 
        return -1 if dp[amount] == float('inf') else dp[amount]
