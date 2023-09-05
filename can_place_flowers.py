from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        valid_spots = 0
        for i in range(len(flowerbed)):
            if (flowerbed[i] == 0
                    and (i == 0 or flowerbed[i - 1] == 0)
                    and (i + 1 == len(flowerbed) or flowerbed[i + 1] == 0)):
                valid_spots += 1
                flowerbed[i] = 1
        return n <= valid_spots


if __name__ == "__main__":
    solution = Solution()
    # print(solution.canPlaceFlowers([1, 0, 0, 0, 1], 1) is True)
    # print(solution.canPlaceFlowers([1, 0, 0, 0, 1], 2) is False)
    # print(solution.canPlaceFlowers([0, 0, 0, 0, 1], 2) is True)
    print(solution.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2) is False)
