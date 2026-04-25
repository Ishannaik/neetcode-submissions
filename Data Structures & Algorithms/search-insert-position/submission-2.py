class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m-1
            else:
                if target == nums[m]:
                    return m
        return l
                #DUMB MISTAKE MADE USED FOR LOOP INSTEAD OF WHILE LOOP!
                # UHH CONFUSSION WHEN TO USE l<=r or l<r cause i am just coding subconciously now and picked l<r and getting confused about it