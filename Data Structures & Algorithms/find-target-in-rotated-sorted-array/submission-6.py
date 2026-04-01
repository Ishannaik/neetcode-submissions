class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        
        while l<r:
            mid =(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        low=l
        if l>0 and target>=nums[0]:
            l,r=0,low-1
        else:
            l,r=low,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] < target:
                l = mid+1
            else:
                r=mid-1
        return -1


                

