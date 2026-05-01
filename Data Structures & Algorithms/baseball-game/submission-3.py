class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for ops in operations:
            if ops == "+":
                stack.append(int(stack[-1])+int(stack[-2]))
            elif ops == "D":
                stack.append(int(stack[-1])*2)
            elif ops == "C":
                stack.pop()
            else:
                stack.append(int(ops))
        return sum(stack)