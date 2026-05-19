class Solution:
    def isValid(self, s: str) -> bool:
        paren_pair = {'{': '}', '[': ']', '(': ')', ')': '(', '}': '{', '[': ']'}
        paren_stack = []
        for i in range(len(s)):
            if s[i] in ['}', ']', ')']:
                if paren_stack:
                    top = paren_stack.pop()
                    if s[i] == '}' and top != '{':
                        return False
                    elif s[i] == ']' and top != '[':
                        return False
                    elif s[i] == ')' and top != '(':
                        return False
                else:
                    return False
            else:
                paren_stack.append(s[i])
        return True if not paren_stack else False