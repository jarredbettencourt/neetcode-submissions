class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        res = 0
        seats.sort()
        students.sort()
        for a, b in zip(seats, students):
            res += abs(a - b)
        return res