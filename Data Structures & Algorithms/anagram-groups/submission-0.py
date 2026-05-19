class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for string in strs:
            sorted_str = ''.join(sorted(string))
            if sorted_str in anagram_map:
                anagram_map[sorted_str].append(string)
            else:
                anagram_map[sorted_str] = [string]
            # anagram_map[sorted_str] = anagram_map.get(sorted_str, []).append(string)
        return list(anagram_map.values())