from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = int((left + right) / 2)
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle

        return -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.search([-1,0,3,5,9,12], 9) == 4)
    print(solution.search([-1,0,3,5,9,12], 2) == -1)
    print(solution.search([5], 5) == 0)
    print(solution.search([5], -5) == -1)
