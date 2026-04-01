class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash_set = set()
        for i in range(len(nums)):
            if nums[i] in hash_set:
                return nums[i]
            else:
                hash_set.add(nums[i])
        return None
