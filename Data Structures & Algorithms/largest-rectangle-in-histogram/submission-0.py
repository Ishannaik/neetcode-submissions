class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for h in range(1,max(heights)+1):
            width = 0
            #now we check if its connected
            for i in range(len(heights)):
                if heights[i] >= h:
                    width+=1
                else:
                    area = h*width
                    max_area = max(area, max_area)
                    width=0
            area = h * width
            max_area = max(max_area, area)
        return max_area