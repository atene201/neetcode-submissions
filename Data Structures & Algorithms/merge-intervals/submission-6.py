class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # edge cases
        # will we be given a valid input guaranteed?
        # duplicate intervals?
        # if so how should we handle that?
        # empty intervals?
        
        # lock down the requirements
        # store result in new list
        # add first interval into that list
        # compare that first interval to the rest of the original list
        # two cases on what can happen?
        # merge two intervals if 
        # start of curr interval is <= end of the prev interval
        # insert current interval into the result list

        intervals.sort(key=lambda pair : pair[0])
        result = [intervals[0]]
        
        for start, end in intervals:
            lastEnd = result[-1][1]

            if start <= lastEnd:
                result[-1][1] = max(lastEnd, end)
            else:
                result.append([start, end])
        return result



