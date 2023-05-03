# Leetcode https://leetcode.com/problems/find-the-difference-of-two-arrays/
# Notes: numbers are repetitive, create sets, return set differences
# JIRA: https://sde2.atlassian.net/browse/UB-71

class Solution:
  # O(n + m) Time | O(n + m) Space, where n and m are length of lists
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)
        return [list(set1 - set2), list(set2 - set1)]
