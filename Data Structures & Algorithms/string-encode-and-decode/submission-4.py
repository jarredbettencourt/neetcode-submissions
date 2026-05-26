class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += f"{len(s)}{s}"
        return encoded_string 

    def decode(self, s: str) -> List[str]:
        decoded_string_arr = []
        i = 0
        print(s)
        while i < len(s):
            decoded_string_arr.append(s[i+1:i+int(s[i])+1])
            i += int(s[i]) + 1
        return decoded_string_arr