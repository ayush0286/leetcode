# Leetcode https://leetcode.com/problems/minimize-maximum-of-array
# Notes: the max value is being shifted towards the index 0, and all numbers are non negative
# JIRA: https://sde2.atlassian.net/browse/UB-6

class Solution:
    # O(n) Time | O(1) Space, where n is length of nums
    def minimizeArrayValue(self, nums: List[int]) -> int:
        prefixSum = nums[0]
        maximumSoFar = nums[0]
        for index in range(1, len(nums)):
            prefixSum += nums[index]
            average = self.ceilDivision(prefixSum, index + 1)
            maximumSoFar = max(maximumSoFar, average)
        return maximumSoFar
        
    # rounds of division to ceiling
    def ceilDivision(self, numerator, denominator):
        return -(numerator // -denominator)
