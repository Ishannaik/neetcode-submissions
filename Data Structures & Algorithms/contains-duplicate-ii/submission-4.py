class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        r = k
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i != j and abs(i-j) <=k:
                    return True
        return False


#BRUTEFORCE DONE