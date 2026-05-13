class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        # are values being pushed positive or negative or both
        self.stack.append(val)
        if self.min is None:
            self.min = val
        if self.min and val < self.min:
            self.min = val

    def pop(self) -> None:
        if self.stack.pop() == self.min:
            if self.stack:
                self.min = min(self.stack)
            else:
                self.min = None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
        
