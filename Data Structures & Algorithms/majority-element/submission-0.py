class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        major = n//2
        res = maxCount = 0
        print(major)
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i,0)+1
            print(hashmap)
            if hashmap[i] > major:
                return i
        print(hashmap)