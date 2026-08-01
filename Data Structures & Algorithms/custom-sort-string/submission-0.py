class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_freq = Counter(s)
        res = ""
        for letter in order:
            if letter in s_freq:
                for _ in range(s_freq[letter]):
                    res += letter
                    s_freq[letter] -= 1
        for k, v in s_freq.items():
            for _ in range(v):
                res += k
        return res