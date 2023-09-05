class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop(0)

    def peek(self) -> int:
        if len(self.output) == 0:
            while self.input:
                self.output.append(self.input.pop(0))
        return self.output[0]

    def empty(self) -> bool:
        return not self.input and not self.output


if __name__ == "__main__":
    solution = MyQueue()
    solution.push(1)
    solution.push(2)
    print(solution.peek() == 1)
    print(solution.pop() == 1)
    print(solution.empty() is False)
    print(solution.pop() == 2)
    print(solution.empty() is True)

    solution = MyQueue()
    print(solution.empty() is True)
