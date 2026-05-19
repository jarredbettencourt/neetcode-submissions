class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        res = []
        digits[-1] = digits[-1] + 1
        for idx, num in enumerate(digits[::-1]):
            if carry == 1:
                num +=1
                carry = 0
            if num == 10:
                res.append(0)
                carry = 1
            else:
                res.append(num)
        if carry == 1:
            res.append(1)
        return res[::-1]