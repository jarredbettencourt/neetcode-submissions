class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_map = {}
        for i in range(len(nums)):
            if (target - nums[i]) in value_map:
                return [value_map[target-nums[i]], i]
            value_map[nums[i]] = i