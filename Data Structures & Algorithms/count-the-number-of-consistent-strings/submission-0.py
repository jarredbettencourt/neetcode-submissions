class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allow_freq = set(allowed)
        res = 0
        for word in words:
            if set(word) <= allow_freq:
                res += 1
        return res