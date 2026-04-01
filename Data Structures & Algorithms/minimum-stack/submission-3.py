class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
        # If it's the first item, it IS the minimum
            new_min = val
        else:
            current_min = self.min_stack[-1]
            new_min = min(val, current_min)
        self.min_stack.append(new_min)


    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
