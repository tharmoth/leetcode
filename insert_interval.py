from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        start_before = 0
        for interval in intervals:
            if newInterval[0] <= interval[0]:
                start_before = interval[0]
                break
            if newInterval[0] <= interval[1]:
                start_before = interval[1]
                break

        end_at = 0
        for interval in intervals:
            if newInterval[1] >= interval[0]:
                end_at = interval[0]
            if newInterval[1] >= interval[1]:
                end_at = interval[1]
            else:
                break

        intervals_to_combine = []
        for interval in intervals:
            if interval[0] <= end_at and interval[1] >= start_before:
                intervals_to_combine.append(interval)

        combined = [intervals_to_combine[0][0], intervals_to_combine[-1][1]]

        if combined[0] > newInterval[0]:
            combined[0] = newInterval[0]

        if combined[1] < newInterval[1]:
            combined[1] = newInterval[1]

        index = intervals.index(intervals_to_combine[0])

        for interval in intervals_to_combine:
            intervals.remove(interval)

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
