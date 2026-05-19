class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_s = {}
        freq_t = {}
        for char in s:
            freq_s[char] = 1 + freq_s.get(char, 0)
        for char in t:
            freq_t[char] = 1 + freq_t.get(char, 0)
        return list(freq_s.values()) == list(freq_t.values())