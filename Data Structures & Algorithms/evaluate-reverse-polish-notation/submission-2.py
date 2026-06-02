class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for n in tokens:
            if n not in {'+', '-', '*', '/'}:
                n = int(n)
                stack.append(n)
            else:
                val1, val2 = stack.pop(), stack.pop()
                if n == '+':
                    stack.append(val1 + val2)
                elif n == '-':
                    stack.append(val2 - val1)                    
                elif n == '*':
                    stack.append(val1 * val2)                    
                elif n == '/':
                    stack.append(int(float(val2) / val1))
        return stack[0]