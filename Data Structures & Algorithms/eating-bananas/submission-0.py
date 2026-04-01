class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        num_piles = len(piles)
        max_pile = max(piles)
        print(max_pile)
        l,r=1,max_pile
        while l<=r:
            mid = (l+r)//2
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / mid)
            if total_hours <= h:
                r = mid - 1
            elif total_hours > h:
                l = mid + 1
        return l