class Solution:
    def isValid(self, s: str) -> bool:
        #so how do we actually track the index?
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []
        if not len(s) % 2 == 0:
            return False
        for bracket in s:
            if bracket in "([{":
                    stack.append(bracket)
            else:
                if stack:
                    if not stack.pop() == mapping[bracket]:
                        return False
                else:
                    return False
        return not stack