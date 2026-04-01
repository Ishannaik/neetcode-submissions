class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l,r=0,len(nums)-1
        temp=0

        while l<=r:
            if nums[l] == val:
               temp = nums[r] 
               nums [r] = nums[l]
               nums [l] = temp
               r-=1
            else:
                l+=1
        return l
