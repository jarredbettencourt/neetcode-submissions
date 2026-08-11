class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        l, r = 0, 0
        while l < len(word) and r < len(abbr):
            if abbr[r] == '0':
                return False
            if word[l] == abbr[r]:
                l += 1
                r += 1
            elif word[l] != abbr[r] and abbr[r].isnumeric():
                sub_length = 0
                while r < len(abbr) and abbr[r].isnumeric():
                    sub_length = sub_length * 10 + int(abbr[r])
                    r += 1
                l += sub_length
                # abbrevaition
            else:
                return False
        return l == len(word) and r == len(abbr)