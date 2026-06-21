class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        word_counts = [Counter(word) for word in words]
        res = []  
        qty = 0
        for letter in word_counts[0]:
            word_in = True
            qty = word_counts[0][letter]
            for word_count in word_counts[1:]:
                if letter not in word_count:
                    word_in = False
                else:
                    qty = min(qty, word_count[letter])
            if word_in:
                for _ in range(qty):
                    res.append(letter)
        return res

                    