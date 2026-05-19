class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def get_euclidean_distance_from_origin(x: int, y: int):
            return x ** 2 + y ** 2
        heap = []
        for x, y in points:
            distance = get_euclidean_distance_from_origin(x, y)
            heapq.heappush(heap, (distance, [x, y]))
        res = []
        while len(res) < k:
                res.append(heapq.heappop(heap)[1])
        return res