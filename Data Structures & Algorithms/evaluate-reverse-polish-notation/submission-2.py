class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}

        stack = []

        for c in tokens:
            if c not in operators:
                stack.append(c)
            else:
                f = int(stack.pop())
                s = int(stack.pop())
                if c == "+":
                    res = f+s
                elif c == "-":
                    res=s-f
                elif c == "*":
                    res=f*s
                elif c == "/":
                    res=s/f
                stack.append(res)
        return int(stack[0])