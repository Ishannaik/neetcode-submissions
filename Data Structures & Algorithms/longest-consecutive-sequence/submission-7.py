class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums =set(nums)
        maxi=0
        if not nums: return 0
        seq={}
        for num in nums:
            if num-1 not in nums: #begning of sequence
                streak = 1
                curr = num

                while curr + 1 in nums:
                    streak +=1
                    curr+=1
                maxi=max(maxi,streak)
            
        return maxi