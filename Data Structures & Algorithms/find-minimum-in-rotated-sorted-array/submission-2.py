class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]>nums[r]:
                #THIS MEANS RIGHT SIDE IS SORTED ARRAY!
                l = mid+1
            else:
                #THIS MEANS LEFT SIDE IS SMALLER MEANING LEFT SIDE IS SORTED ARRAY!
                r = mid
        return nums[l]
