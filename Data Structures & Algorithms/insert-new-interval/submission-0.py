class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:


        intervals.append(newInterval)

        intervals.sort(key=lambda i : i[0])

        result = [intervals[0]]


        for i in range(1, len(intervals)):
            prev_end_time = result[-1][1]
            curr_start_time = intervals[i][0]

            if curr_start_time <= prev_end_time:
                start_time = min(curr_start_time, result[-1][0])
                end_time = max(prev_end_time, intervals[i][1])
                result.pop()
                result.append([start_time, end_time])
            else:
                result.append(intervals[i])

        return result