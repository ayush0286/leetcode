# Leetcode https://leetcode.com/problems/meeting-rooms-ii
# Notes: sort the start and end indexes and use two pointers to calculate max concurrent meetings
# JIRA: https://sde2.atlassian.net/browse/UB-42

class Solution:
    #O(nlogn) Time | O(n) Space, where n is length of intervals 
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = [interval[0] for interval in intervals]
        ends = [interval[1] for interval in intervals]
        
        starts.sort()
        ends.sort()
        maxCount = 0
        count = 0
        endIdx = 0
        startIdx = 0
        while startIdx < len(starts):
            if starts[startIdx] < ends[endIdx]:
                count += 1
                maxCount = max(maxCount, count)
                startIdx += 1
                continue
            else:
                count -= 1
                endIdx += 1
        return maxCount
