class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x: len(x))
        res = []
        for idx, string in enumerate(words):
            cont_string = string
            for i in range(idx + 1, len(words)):
                if cont_string in words[i]:
                    res.append(cont_string)
                    break
        return res