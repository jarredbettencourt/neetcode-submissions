class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def get_euclidean_distance_from_origin(x: int, y: int):
            return math.sqrt(x ** 2 + y ** 2)
            
        heap = []
        distance_map = defaultdict(list)
        for point in points:
            distance = get_euclidean_distance_from_origin(point[0], point[1])
            heapq.heappush(heap, distance)
            distance_map[distance].append(point)
        res = []
        while len(res) < k:
            distance = heapq.heappop(heap)
            res.append(distance_map[distance].pop())
        return res