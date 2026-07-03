class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minval = min(self.prefix[-1], val) if self.prefix else val
        self.prefix.append(minval)

    def pop(self) -> None:
        self.prefix.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefix[-1]
