class MinStack:

    def __init__(self):
        self.stack = []
        self.ministack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        cur_mini = min(val, self.ministack[-1] if self.ministack else val)
        self.ministack.append(cur_mini)

    def pop(self) -> None:
        self.stack.pop()
        self.ministack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.ministack[-1]
