class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r= len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r]>target:
                print(numbers[l],numbers[r])
                r-=1
            elif numbers[l]+numbers[r]==target:
                break
            else:
                print(numbers[l],numbers[r])
                l+=1
        return [l+1,r+1]