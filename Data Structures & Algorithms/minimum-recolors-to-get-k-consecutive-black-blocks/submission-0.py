class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = float('inf')
        for i in range(len(blocks) - k + 1):
            res = min(blocks[i:i+k].count('W'), res)
        return res