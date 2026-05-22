class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        res = -1
        cont_set = set(range(1, n + 1))
        test_set = set() 
        for e in trust:
            test_set.add(e[0])

        valid_set = cont_set - test_set
        return -1 if not valid_set else list(valid_set)[0]