class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # s_len = len(s)
        # res = 0
        # for i in range(s_len - 1, -1, -1):
        return len(s.split()[-1])