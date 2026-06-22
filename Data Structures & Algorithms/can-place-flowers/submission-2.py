class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Padding helps, because 0 is like an or here
        # Regardless of padding, flowerbed[0] can only be padded if flowerdbed[i+1] is a 0
        count = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                count += 1
                flowerbed[i] = 1
        return count >= n