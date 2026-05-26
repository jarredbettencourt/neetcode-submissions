class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dictionary = {}
        for idx, letter in enumerate(order):
            dictionary[letter] = idx
        for i in range(1, len(words)):
            word_one, word_two = words[i-1], words[i]
            for j in range(len(word_one)):
                if j == len(word_two):
                    return False 
                if word_one[j] != word_two[j]:
                    if dictionary[word_one[j]] > dictionary[word_two[j]]:
                        return False
                    break
        return True