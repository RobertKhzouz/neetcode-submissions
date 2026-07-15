class MinStack:

    def __init__(self):
        self.stack = []
        self.prefixes = []
        self.counter = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) > 1:
            smaller = len(self.prefixes) if val <= self.stack[self.prefixes[len(self.prefixes) - 1]] else self.prefixes[len(self.prefixes) - 1]
            self.prefixes.append(smaller)
        else:
            self.prefixes.append(0)
        self.counter += 1

        if self.counter == 4:
            print(self.stack)
            print(self.prefixes)
            print()

    def pop(self) -> None:
        self.stack.pop()
        self.prefixes.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.stack[self.prefixes[len(self.prefixes) - 1]]