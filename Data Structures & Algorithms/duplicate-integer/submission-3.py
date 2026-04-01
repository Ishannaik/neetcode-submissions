class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list1 = list(dict.fromkeys(nums))
        print(list1)
        if list1==nums:
            print(list1)
            print(nums)
            return False
        else:
            print(list1)
            print(nums)
            return True

