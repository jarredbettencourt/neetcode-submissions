class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        def maxWater(l, r, heights):
            return (r - l) * min(heights[r], heights[l])
        maxWaterScalar = 0
        while l < r:
            maxWaterScalar = max(maxWaterScalar, maxWater(l, r, heights))
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        return maxWaterScalar