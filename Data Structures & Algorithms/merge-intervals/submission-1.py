class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        new_intervals = [intervals[0]]
        for i in range(1, len(intervals)):
            endTime = new_intervals[-1][1]
            if endTime >= intervals[i][0]:
                new_intervals[-1] = [min(intervals[i][0], new_intervals[-1][0]), max(intervals[i][1], endTime)]
            else:
                new_intervals.append(intervals[i])
        return new_intervals