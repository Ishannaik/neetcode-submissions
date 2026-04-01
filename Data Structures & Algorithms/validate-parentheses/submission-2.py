class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {'[':']','(':')','{':'}'}
        stack =[]
        for brac in s:
            if (brac == '[') or (brac =='{') or (brac=='('):
                stack.append(brac)
            elif stack:
                popped_bracket = stack.pop()
                if dictionary[popped_bracket] != brac:
                   return False
            else:
                return False
            
        return len(stack) == 0

                



