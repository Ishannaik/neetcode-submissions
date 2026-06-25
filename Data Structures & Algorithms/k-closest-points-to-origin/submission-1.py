class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        result  = []
        heapq.heapify(arr)
        for p in points:
            x, y = p
            dist = x * x + y * y
            heapq.heappush(arr,(dist, p))
        for i in range(k):
            dist, point = heapq.heappop(arr)
            result.append(point)
        return result

