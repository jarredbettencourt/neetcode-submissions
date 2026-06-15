class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_counter = Counter(text)
        b_count = text_counter["b"]
        a_count = text_counter["a"]
        l_count = text_counter["l"]
        o_count = text_counter["o"]
        n_count = text_counter["n"]
        return min(b_count, a_count, l_count, o_count, n_count)