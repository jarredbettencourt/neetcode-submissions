class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq_list = collections.Counter(arr)
        # 3:3, 2:2, 1:1
        max_lucky_integer = -1
        for num, count in freq_list.items():
            # 3:3
            if num == count:
                max_lucky_integer = max(max_lucky_integer, num)
        return max_lucky_integer