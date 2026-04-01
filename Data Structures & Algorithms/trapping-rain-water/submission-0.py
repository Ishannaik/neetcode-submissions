class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0] * n
        prefix[0] = height[0]
        suffix = [0] * n
        suffix[-1] = height[-1]
        total=0
        for i in range(1,n):
            prefix[i] = max(prefix[i-1],height[i])
        print(prefix)
        for i in range(n-2, -1, -1):
            suffix[i] = max(suffix[i+1], height[i])
        for i in range(1,n):
            total = total + (min(prefix[i],suffix[i]) - height[i])
        return total

