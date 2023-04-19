# Leetcode https://leetcode.com/problems/optimal-partition-of-string
# Notes: minimum number of substring dictates splitting string at duplicates
# JIRA: https://sde2.atlassian.net/browse/UB-5


class Solution:
    # O(n) Time | O(1) Space, where n is length of s
    def partitionString(self, s: str) -> int:
        stringCount = 0
        seen = {}
        for char in s:
            if char in seen:
                seen = {char : True}
                stringCount += 1
            else:
                seen[char] = True
        return stringCount + 1
