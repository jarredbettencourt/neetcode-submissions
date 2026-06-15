class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_counter = Counter(text)
        return min(text_counter['b'], text_counter['a'], text_counter['n']) if Counter("balloon") <= text_counter else 0
