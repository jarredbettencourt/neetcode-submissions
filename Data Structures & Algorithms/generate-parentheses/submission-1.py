class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def is_valid(l):
            return len(l) == 2*n and l.count('(') == l.count(')')

        def dfs(path):
            if is_valid(path):
                res.append("".join(path.copy()))
                return

            path.append('(')
            dfs(path)
            path.pop()
            path.append(')')
            dfs(path)
            path.pop()


        dfs([])

        return res