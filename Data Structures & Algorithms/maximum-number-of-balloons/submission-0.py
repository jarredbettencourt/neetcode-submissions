class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_counter = Counter(text)
        balloon_found = True
        res = float('inf')
        for letter in "balloon":
            if letter in text_counter:
                res = min(res, text_counter[letter])
            else:
                balloon_found = False
        return 0 if not balloon_found else res