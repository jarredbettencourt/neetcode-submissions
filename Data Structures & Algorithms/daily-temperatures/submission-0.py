class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                temp_stack, idx_stack = stack.pop()
                res[idx_stack] = idx - idx_stack
            stack.append((temp, idx))
        return res