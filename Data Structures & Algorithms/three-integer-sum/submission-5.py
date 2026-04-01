class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        res=[]
        nums.sort()
        for l in range(len(nums)-2):
            if l > 0 and nums[l] == nums[l - 1]:
                continue
            s=l+1
            r= len(nums)-1
            while s<r:
                sum = nums[l] + nums[s] + nums[r]
                if sum > 0:
                    r-=1
                elif sum < 0:
                    s+=1
                else:
                    res.append([nums[l],nums[s],nums[r]])
                    s += 1
                    r -= 1
                    while s < r and nums[s] == nums[s - 1]:
                        s += 1
                    while s < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res
                    