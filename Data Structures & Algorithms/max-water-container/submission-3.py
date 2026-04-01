class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        d=r-l+1
        max=0
        while l<r:
            d = r-l
            min_heights = min(heights[l],heights[r])
            curr_heights = d * min_heights
            if curr_heights>max:
                max = curr_heights
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max
                