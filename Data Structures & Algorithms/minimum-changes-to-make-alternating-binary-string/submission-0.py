class Solution:
    def minOperations(self, s: str) -> int:
        # at most len(s) // 2
        res_zero, res_one = 0, 0
        for i in range(len(s)):
            # at an even index
            if (i % 2) == 0:
                res_zero += (1 if s[i] == '1' else 0)
                res_one += (1 if s[i] == '0' else 0)
            else:
                res_zero += (1 if s[i] == '0' else 0)
                res_one += (1 if s[i] == '1' else 0)
        return min(res_one, res_zero)