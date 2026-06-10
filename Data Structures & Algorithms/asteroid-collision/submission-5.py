class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for idx, value in enumerate(asteroids):
            stack.append(value)
            while (len(stack) >= 2) and ((stack[-2] > 0 and stack[-1] < 0) or (stack[-2] < 0 and stack[-1] > 0)):
                val1 = stack.pop()
                val2 = stack.pop()
                if abs(val1) == abs(val2):
                    continue
                elif abs(val1) > abs(val2):
                    stack.append(val1)
                elif abs(val2) > abs(val1):
                    stack.append(val2)
        return stack