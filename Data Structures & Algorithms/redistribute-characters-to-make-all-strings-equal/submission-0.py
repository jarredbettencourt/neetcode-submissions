class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        total_dict = {}
        for word in words:
            letter_freq = Counter(word)
            for letter in letter_freq:
                if letter in total_dict:
                    total_dict[letter] += letter_freq[letter]
                else:
                    total_dict[letter] = letter_freq[letter]
            
        for letter, freq in total_dict.items():
            if freq % len(words) != 0:
                return False
        return True