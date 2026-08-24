class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}
        for i in range(n):
            adj[i] = []
        for s, dst, weight in edges:
            adj[s].append((dst, weight))
        distances = {}
        min_heap = [(0, src)]
        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in distances:
                continue
            distances[n1] = w1
            for n2, w2 in adj[n1]:
                if n2 not in distances:
                    heapq.heappush(min_heap, (w1 + w2, n2))
        print(distances)
        return distances