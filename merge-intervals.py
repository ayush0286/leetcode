class Solution:
    # O(nlogn) Time | O(m) Space, where n is length of intervals 
    # and m is mergedIntervals length
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        # curr end < next start, add
        # curr end >= next start, merge
        # new curr end = max(next end, end)
        mergedIntervals = []
        if len(intervals) <= 1:
            return intervals
        
        start = intervals[0][0]
        end = intervals[0][1]
        for interval in intervals[1:]:
            nextStart = interval[0]
            nextEnd = interval[1]
            if end < nextStart:
                mergedIntervals.append([start, end])
                start = nextStart
                end = nextEnd
            else: # end >= nextStart
                end = max(end, nextEnd)
        mergedIntervals.append([start, end])
        return mergedIntervals
