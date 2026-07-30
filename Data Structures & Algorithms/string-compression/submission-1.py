class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = 0
        while i < len(chars):
            cur_length = 1
            cur_char = chars[i]
            j = i + 1
            while j < len(chars) and chars[j- 1] == chars[j]:
                cur_length += 1
                j += 1
            if cur_length == 1:
                res += 1
                i += 1
                continue
            char_insert = str(cur_char) + str(cur_length)
            print(char_insert)
            for k in range(len(char_insert)):
                chars[k + res] = char_insert[k]
            res += len(char_insert) 
            # print(chars)
            i += cur_length
        return res