class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums_freq = Counter(nums)
        res = 0
        for k in nums_freq:
            while nums_freq[k] != 0:
                print(nums_freq)
            # need to get factorization
                if nums_freq[k] == 1:
                    return -1
                elif nums_freq[k] % 3 == 0:
                    res += (nums_freq[k] // 3)
                    nums_freq[k] = 0
                elif nums_freq[k] % 2 == 0:
                    res += (nums_freq[k] // 2)
                    nums_freq[k] = 0
                else:
                    res += 1
                    nums_freq[k] -= 3
        return res