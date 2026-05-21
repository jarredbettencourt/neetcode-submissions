class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = 0
        stack = []
        for n in operations:
            if n == 'C':
                stack.pop()
            elif n == 'D':
                stack.append(int(stack[-1]) * 2)
            elif n == '+':
                stack.append(int(stack[-1]) + int(stack[-2]))
            else:
                stack.append(int(n))
        return sum(stack)