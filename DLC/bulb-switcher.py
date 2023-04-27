# Leetcode https://leetcode.com/problems/bulb-switcher
# Notes: every col is toggled even times unless it's a square of an int
# JIRA: https://sde2.atlassian.net/browse/UB-64

class Solution:
    # O(n) Time | O(1) Space
    def bulbSwitch(self, n: int) -> int:
        if n == 0:
            return 0
        onCount = 0
        index = 1
        while index * index <= n:
            onCount += 1
            index += 1
        return onCount
