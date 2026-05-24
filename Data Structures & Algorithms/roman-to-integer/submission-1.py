class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        value_mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 100
        }
        stack = []
        for num in s:
            num_mapping = value_mapping[num]
            print(stack)
            if stack:
                if stack[-1] < num_mapping:
                    val = stack.pop()
                    stack.append(num_mapping - val)
                else:
                    stack.append(num_mapping)
            else:
                stack.append(num_mapping)
        return sum(stack)