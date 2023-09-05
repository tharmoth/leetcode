from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5)
    print(solution.maxProfit([7, 6, 4, 3, 1]) == 0)
    print(solution.maxProfit([1, 2]) == 1)
    print(solution.maxProfit([2, 1, 2, 0, 1]) == 1)
    print(solution.maxProfit([2, 1, 2, 1, 0, 1, 2]) == 2)
    print(solution.maxProfit([3, 2, 1, 5, 0, 2]) == 4)
