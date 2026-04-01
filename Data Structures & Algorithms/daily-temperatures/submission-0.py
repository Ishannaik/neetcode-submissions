class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            a = 0
            for j in range(i + 1, len(temperatures)):
                a += 1
                if temperatures[i] < temperatures[j]:
                    result.append(a)
                    break
            else:
                result.append(0)
        return result
## BRUTEFORCE