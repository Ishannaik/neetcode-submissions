class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,x in enumerate(nums):
            difference = target - nums[i]
            if difference in seen:
                return [seen[difference], i]
            seen[x] = i