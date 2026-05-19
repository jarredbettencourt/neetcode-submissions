class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        def pascal_map(arr):
            res = []
            res.append(1)
            for i in range(1, len(arr)):
                res.append(arr[i] + arr[i-1])
            res.append(1)
            return res
        
        res = [[1]]
        while len(res) != numRows:
            res.append(pascal_map(res[-1]))
        return res