class MinStack:

    def __init__(self):
        self.stack = []
        self.min_index = 0

    def push(self, val: int) -> None:
        if isinstance(val, int):
            self.stack.append(val)
            if val < self.stack[self.min_index]:
                self.min_index = len(self.stack) - 1

    def pop(self) -> None:
        self.stack.pop()
        if self.min_index == len(self.stack):
            self.min_index = 0
            for i, val in enumerate(self.stack):
                if val < self.stack[self.min_index]:
                    self.min_index = i

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.stack[self.min_index]