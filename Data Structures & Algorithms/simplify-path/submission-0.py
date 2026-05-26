class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        for p in path:
            if not p:
                continue
            if stack:
                if p == '..':
                    stack.pop()
                    continue
                elif p == '.':
                    continue
            stack.append(p)


        return "/" + "/".join(stack)
