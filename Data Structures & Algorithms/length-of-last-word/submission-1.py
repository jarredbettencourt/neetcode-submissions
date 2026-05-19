class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_len = len(s)
        res = 0
        # for i in range(s_len - 1, -1, -1):
        i = s_len - 1
        while s[i] == ' ':
            i -= 1
        while s[i] != ' ':
            res += 1
            i -= 1
        return res
        # return len(s.split()[-1])