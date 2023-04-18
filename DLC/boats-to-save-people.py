# Leetcode https://leetcode.com/problems/boats-to-save-people
# Notes: sort people, two pointers, since limit > people[i] evaluate right + left less than limit
# JIRA: https://sde2.atlassian.net/browse/UB-4

class Solution:
# O(nlogn) Time | O(1) Space, where n is length of people
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0 
        right = len(people) - 1
        boatCount = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            boatCount += 1
        return boatCount
