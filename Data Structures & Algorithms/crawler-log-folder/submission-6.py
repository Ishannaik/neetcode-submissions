class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for l in logs:
            print(l, res)
            if l == "../":
                if res !=0:
                    res-=1
            elif l == "./":
                pass
            else:
                res+=1
        return res