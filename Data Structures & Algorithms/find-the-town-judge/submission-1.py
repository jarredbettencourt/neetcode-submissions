class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        res = -1
        # [how many they trust, how many trust them]
        degrees = [[0, 0] for _ in range(n + 1)]
        for person in trust:
            degrees[person[0]][0] += 1
            degrees[person[1]][1] += 1

        print(degrees)
        for idx, degree in enumerate(degrees):
            if degree[0] == 0 and degree[1] == n - 1:
                return idx
        return res