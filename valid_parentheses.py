class Solution:

    opening = ['(', '[', '{']
    closing = [')', ']', '}']

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in self.opening:
                stack.append(c)
            else:
                if len(stack) == 0 or self.opening.index(stack.pop()) != self.closing.index(c):
                    return False

        return len(stack) == 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid('()') is True)
    print(solution.isValid('()[]{}') is True)
    print(solution.isValid('(]') is False)
    print(solution.isValid('([])') is True)
    print(solution.isValid('([)]') is False)
    print(solution.isValid(']') is False)
