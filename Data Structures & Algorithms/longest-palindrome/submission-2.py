class Solution:
    def longestPalindrome(self, s: str) -> int:
        word_freq = Counter(s)
        res = 0
        one = True
        for letter, freq in word_freq.items():
            if freq % 2 == 0:
                res += freq
            else:
                if freq == 1 and one:
                    res += 1
                    one = False
                else:
                    res += (freq - 1)
        return res