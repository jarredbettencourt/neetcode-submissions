class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = {}
        t_freq = {}
        for n in s:
            s_freq[n] = 1 + s_freq.get(n, 0)
        for n in t:
            t_freq[n] = 1 + t_freq.get(n, 0)
        return s_freq == t_freq