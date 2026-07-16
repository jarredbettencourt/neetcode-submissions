class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # find point where top sandwich is 0 and there are no 1 students, or top sandwich is 1 and there are no 0 students
        student_count = Counter(students)
        sandwich_count = Counter(sandwiches)
        for i, sandwich in enumerate(sandwiches):
            if student_count[sandwich] == 0:
                return len(sandwiches) - i
            else:
                student_count[sandwich] -= 1
        return 0
