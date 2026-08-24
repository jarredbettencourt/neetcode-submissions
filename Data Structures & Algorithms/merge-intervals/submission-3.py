class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                # merge
                res[-1] = [min(res[-1][0], intervals[i][0]), intervals[i][1]]
            else:
                res.append(intervals[i])
        return res