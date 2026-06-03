class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        stack = []
        level = 0
        for log in logs:
            if log == '../':
                level-=1
            elif log == './':
                pass
            else:
                level +=1
        return level