from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        base_color = image[sr][sc]
        image[sr][sc] = color
        for i_r, i_c in zip([sr + 1, sr - 1, sr, sr], [sc, sc, sc - 1, sc + 1]):
            if (0 <= i_r < len(image)
                    and 0 <= i_c < len(image[0])
                    and image[i_r][i_c] == base_color
                    and image[i_r][i_c] != color):
                image = self.floodFill(image, i_r, i_c, color)

        return image


if __name__ == "__main__":
    solution = Solution()
    print(solution.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]])
    print(solution.floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 0) == [[0, 0, 0], [0, 0, 0]])
