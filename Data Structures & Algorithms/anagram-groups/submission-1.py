class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        # for string in strs:
        #     sorted_str = ''.join(sorted(string))
        #     if sorted_str in anagram_map:
        #         anagram_map[sorted_str].append(string)
        #     else:
        #         anagram_map[sorted_str] = [string]
        #     # anagram_map[sorted_str] = anagram_map.get(sorted_str, []).append(string)
        # return list(anagram_map.values())
        

        # for each string in strs
        # make a freq table
        # hash by that freq table (somehow)
        for string in strs:
            freq_map = [0] * 26
            for c in string:
                freq_map[ord(c) - ord('a')] += 1 
            freq_map = str(freq_map)
            if freq_map not in anagram_map:
                anagram_map[freq_map] = [string]
            else:
                anagram_map[freq_map].append(string)
        return list(anagram_map.values())   