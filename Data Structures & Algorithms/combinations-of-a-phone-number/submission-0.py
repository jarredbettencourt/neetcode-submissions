class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        def backtrack(digit, path):
            if len(path) == len(digits):
                res.append(path)
                return
            n = digit[0]
            digit_letters = digit_map[n]
            for letter in digit_letters:
                backtrack(digit[1:], path + letter)
        backtrack(digits, "")
        return res