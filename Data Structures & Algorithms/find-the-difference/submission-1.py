class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_freq = collections.Counter(s)
        t_freq = collections.Counter(t)
        for letter in t_freq:
            if (letter not in s_freq) or (letter in s_freq and s_freq[letter] != t_freq[letter]):
                return letter