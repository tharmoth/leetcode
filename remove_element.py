
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        offset = 0
        for i in range(len(nums)):
            if nums[i] == val:
                offset += 1
            else:
                nums[i - offset] = nums[i]
        return len(nums) - offset


if __name__ == "__main__":
    solution = Solution()
    # print(solution.removeElement([3, 2, 2, 3], 3) == 2)
    print(solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5)
    print(solution.removeElement([1], 1) == 0)
    print(solution.removeElement([1, 1], 1) == 0)
