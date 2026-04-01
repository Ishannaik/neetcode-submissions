class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest_streak=0

        for num in s: #SSEQUENCE STARTER CODE
            if num-1 not in s:
                current_num = num
                current_streak=1

                while current_num + 1 in s:
                    current_streak=current_streak+1
                    current_num=current_num+1
                longest_streak = max(longest_streak,current_streak)
        return longest_streak

