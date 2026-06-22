class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_mapping = {}
        for char_a, char_b in zip(s, t):
            if char_a in char_mapping and char_mapping[char_a] != char_b:
                return False
            char_mapping[char_a] = char_b 
        char_mapping = {}
        for char_a, char_b in zip(t, s):
            if char_a in char_mapping and char_mapping[char_a] != char_b:
                return False
            char_mapping[char_a] = char_b 
        return True