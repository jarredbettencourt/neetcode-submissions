class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        res = 0
        for word in words:
            if Counter(word) <= chars_count:
                res += len(word)
        return res