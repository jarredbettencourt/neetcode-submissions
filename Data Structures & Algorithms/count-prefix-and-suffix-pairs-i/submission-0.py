class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    # print(words[i])
                    # print(words[j])
                    res += 1
        return res