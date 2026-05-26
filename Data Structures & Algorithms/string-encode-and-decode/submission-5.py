class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += f"{len(s)}#{s}"
        return encoded_string 

    def decode(self, s: str) -> List[str]:
        decoded_string_arr = []
        i = 0
        print(s)
        while i < len(s):
            enc_length = ""
            while s[i] != '#':
                enc_length += s[i]
                i+=1
            print(enc_length)
            decoded_string_arr.append(s[i+1:i+1+int(enc_length)])
            i += int(enc_length) + 1
        return decoded_string_arr