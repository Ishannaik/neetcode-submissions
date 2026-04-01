class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            if i in operators:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if i == "+":
                    result = num1 + num2
                elif i == "-":
                    result = num1 - num2
                elif i == "*":
                    result = num1 * num2
                elif i == "/":
                     result = int(num1 / num2)  
                stack.append(result)



        return stack[0]