import math
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total_max = -math.inf
        current = 0

        for num in nums:
            current = max(current + num, num)
            total_max = max(current, total_max)

        return total_max


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6)
    print(solution.maxSubArray([1]) == 1)
    print(solution.maxSubArray([5,4,-1,7,8]) == 23)
    print(solution.maxSubArray([-2,-1]) == -1)
    print(solution.maxSubArray([-2,1]) == 1)

