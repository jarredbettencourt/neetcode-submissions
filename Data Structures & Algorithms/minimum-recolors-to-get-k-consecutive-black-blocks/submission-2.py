class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Brute force
        # res = float('inf')
        # for i in range(len(blocks) - k + 1):
        #     res = min(blocks[i:i+k].count('W'), res)
        # return res

        w_count = 0
        for i in range(k):
            if blocks[i] == 'W':
                w_count += 1
        res = w_count

        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                w_count += 1
            if blocks[i - k] == 'W':
                w_count -= 1
            res = min(w_count, res)
        return res
