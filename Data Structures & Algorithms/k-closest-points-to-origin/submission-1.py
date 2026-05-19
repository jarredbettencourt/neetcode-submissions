class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def get_euclidean_distance_from_origin(x: int, y: int):
            return x ** 2 + y ** 2
        heap = []
        for point in points:
            distance = get_euclidean_distance_from_origin(point[0], point[1])
            heapq.heappush(heap, (distance, [point[0], point[1]]))
        res = []
        while len(res) < k:
                res.append(heapq.heappop(heap)[1])
        return res