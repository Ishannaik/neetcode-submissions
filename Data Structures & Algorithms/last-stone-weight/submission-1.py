class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        print(stones)
        heapq.heapify(stones)
        print(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            print(first)
            second = heapq.heappop(stones)
            print(second)
            if second > first:
                heapq.heappush(stones, first - second)
        stones.append(0)
        return abs(stones[0])
