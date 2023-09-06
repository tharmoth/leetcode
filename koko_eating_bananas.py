from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            middle = int((left + right) / 2)
            if self.check(piles, h, middle):
                right = middle
            else:
                left = middle + 1

        return left

    def check(self, piles: List[int], h: int, num: int) -> int:
        return sum(math.ceil(pile / num) for pile in piles) <= h


if __name__ == "__main__":
    solution = Solution()
    print(solution.minEatingSpeed([3, 6, 7, 11], 8) == 4)
    print(solution.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30)
    print(solution.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23)
