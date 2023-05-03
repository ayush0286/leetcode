# Leetcode https://leetcode.com/problems/find-the-difference-of-two-arrays/
# Notes: numbers are repetitive, create sets, return set differences
# JIRA: https://sde2.atlassian.net/browse/UB-71

class Solution:
  # O(n + m) Time | O(n + m) Space, where n and m are length of lists
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = {}
        set2 = {}
        for num in nums1:
            set1[num] = True
        for num in nums2:
            set2[num] = True
        
        distincts = [[], []]
        for num1 in set1:
            if num1 not in set2:
                distincts[0].append(num1)
        for num2 in set2:
            if num2 not in set1:
                distincts[1].append(num2)
        return distincts
