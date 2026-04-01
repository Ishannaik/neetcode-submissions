class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
        
            prod=1
            print(nums[i],end="")
            print(nums[i+1:],end="")
            print(nums[:i],end="")
            print()
            for j in range(len(nums)):
                if not i == j:
                   prod = prod * nums[j] 
                   print(prod)
            output.append(prod)
        return output