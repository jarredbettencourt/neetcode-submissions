class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        def vowel_begin_end(word):
            vowels = {'a', 'e', 'i', 'o', 'u'}
            if word[0] in vowels and word[-1] in vowels:
                return True
            return False
        
        prefix_list = [0] * len(words)

        if vowel_begin_end(words[0]):
            prefix_list[0] = 1

        for i in range(1, len(words)):
            prefix_list[i] = prefix_list[i-1] + (1 if vowel_begin_end(words[i]) else 0)
        
        res = []

        for query in queries:
            if query[0] == 0:
                res.append(prefix_list[query[1]])
            elif query[0] == query[1]:
                res.append(prefix_list[query[1]] - prefix_list[query[1] - 1])
            else:
                res.append(prefix_list[query[1]] - prefix_list[query[0]])
        return res
