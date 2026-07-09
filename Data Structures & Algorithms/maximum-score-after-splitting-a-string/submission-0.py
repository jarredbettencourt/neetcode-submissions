class Solution:
    def maxScore(self, s: str) -> int:
        l_score, r_score = s[0].count('0'), s[1:].count('1')
        res = l_score + r_score
        for i in range(1, len(s)):
            if s[i] == '1':
                r_score -= 1
            else:
                l_score += 1
            res = max(res, l_score + r_score)
        return res