class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=0
        final_list=[]
        for i in numbers: #1 
            for j in numbers: #2
                if (i+j)==target and j>i:
                    final_list.append(numbers.index(i)+1)
                    final_list.append(numbers.index(j)+1)
                    break
                r=r+1
            l=l+1
        return final_list
