class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # what does an overlapping interval mean
        # [1, 2] and [3, 4] not overlapping
        # [1, 2] and [2, 3] are overlapping

        # end_time from the 1st interval = start_time from the second interval

        # [[]] : [[]]
        # [1, 2][2, 2] -> [1,2] ? yes
        # [1, 2][2, 2][0, 0] -> [0,2]? yes

        # intervals sorted based on start_time
        # ex.[1, 2][3, 4][2, 3] -> [1, 2][2, 3][3, 4]
        # if end_time from the 1st interval <= start_time from the second interval
        # overlapping -> [start_time from the first interval, end_time from the second_interval]
        # not overlapping -> add that interval to the resulting array

        intervals.sort(key=lambda i: i[0])
        result = [intervals[0]]

        # [1, 3][2, 4][4, 5]
        for i in range(1, len(intervals)):
            prev_end_time = result[-1][1]
            next_start_time= intervals[i][0]

            # [1,2] [0,3]: [0,3]
            if next_start_time <= prev_end_time:
                start_time = min(result[-1][0], intervals[i][0])
                end_time = max(result[-1][1], intervals[i][1])
                result.pop()
                result.append([start_time, end_time])
            else:
                result.append(intervals[i])
        return result




