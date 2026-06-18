class NumArray:

    def __init__(self, nums: List[int]):
        self.sum_array = [0] * (len(nums))
        cur = 0
        for i in range(len(nums)):
            cur += nums[i]
            self.sum_array[i] = cur
        print(self.sum_array)


    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sum_array[right]
        return self.sum_array[right] - self.sum_array[left - 1]
# [a, b, c, d]
# [a, a+b, a+b+c, a+b+c+d]
# range(3, 1)
# a + b + c + d - (a + b) = c + d
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)