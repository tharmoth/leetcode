import sys
from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        # This can be cleaned up a great deal.
        intervals_to_combine = []
        start_before = -1
        end_at = -1
        index = len(intervals)
        for interval in intervals:
            if newInterval[0] <= interval[1] and start_before == -1:
                start_before = interval[1]
                index = intervals.index(interval)
            elif newInterval[0] <= interval[0] and start_before == -1:
                start_before = interval[0]
                index = intervals.index(interval)

            if newInterval[1] < interval[0] and end_at == -1:
                end_at = interval[0]
            elif newInterval[1] < interval[1] and end_at == -1:
                end_at = interval[1]

            if (interval[0] < end_at or end_at == -1) and (interval[1] >= start_before != -1):
                intervals_to_combine.append(interval)

        combined = [min(newInterval[0], intervals_to_combine[0][0] if len(intervals_to_combine) > 0 else sys.maxsize),
                    max(newInterval[1], intervals_to_combine[-1][1] if len(intervals_to_combine) > 0 else 0)]

        for interval in intervals_to_combine:
            intervals.remove(interval)

        if not end_at:
            index = len(intervals)

        intervals.insert(index, combined)

        return intervals


if __name__ == "__main__":
    solution = Solution()
    print(solution.insert([], [2, 5]) == [[2, 5]])
    print(solution.insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]])
    print(solution.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]])
    print(solution.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [1, 2]) == [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]])
    print(solution.insert([[1, 2], [4, 5], [6, 7], [8, 10], [12, 16]], [1, 3]) == [[1, 3], [4, 5], [6, 7], [8, 10],
                                                                                   [12, 16]])

    print(solution.insert([[10, 11], [12, 13]], [1, 2]) == [[1, 2], [10, 11], [12, 13]])
    print(solution.insert([[10, 11], [12, 13]], [100, 200]) == [[10, 11], [12, 13], [100, 200]])
    print(solution.insert([[0,0],[1,4],[6,8],[9,11]], [0,9]) == [[0,11]])
    print(solution.insert([[0, 0]], [0, 0]) == [[0, 0]])