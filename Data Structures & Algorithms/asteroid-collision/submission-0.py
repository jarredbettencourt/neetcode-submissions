class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for idx, ast in enumerate(asteroids):
            if stack:
                top = stack[-1]
                if ast > 0 and top > 0 or ast < 0 and top < 0:
                    stack.append(ast)
                if ast < 0 and top > 0 and abs(ast) < abs(top):
                    continue
                if ast > 0 and top < 0 and abs(top) > abs(ast):
                    stack.pop()
                    stack.append(ast)
                if ast > 0 and top < 0 or ast < 0 and top > 0 and abs(ast) == abs(top):
                    stack.pop()
                    continue
            else:
                stack.append(ast)
        return stack