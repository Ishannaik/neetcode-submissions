class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()

            biggest = stones.pop()
            second_biggest = stones.pop()

            if biggest != second_biggest:
                stones.append(biggest - second_biggest)
            
        return stones[0] if stones else 0