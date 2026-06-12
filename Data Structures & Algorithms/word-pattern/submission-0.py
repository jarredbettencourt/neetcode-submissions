class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        assoc_map = {}
        s = s.split()
        for char, word in zip(pattern, s):
            if char in assoc_map and assoc_map[char] != word:
                return False
            assoc_map[char] = word
        return True
            