class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list1 = list(dict.fromkeys(nums))
        if list1==nums:
            return False
        else:
            return True

