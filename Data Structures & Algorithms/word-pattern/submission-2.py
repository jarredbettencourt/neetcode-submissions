class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_map = {}
        s_map = {}
        s = s.split()
        if len(s) != len(pattern):
            return False
        for char, word in zip(pattern, s):
            if (word in s_map and s_map[word] != char) or (char in pattern_map and pattern_map[char] != word):
                return False
            pattern_map[char] = word
            s_map[word] = char
        return True
            