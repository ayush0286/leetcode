# Leetcode https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome
# Notes: what choices do we have when comparing two chars to make it a palindrome
# JIRA: https://sde2.atlassian.net/browse/UB-51

class Solution:
    # O(n^2) Time | O(n) Space, where n is length of s
    def minInsertions(self, s: str) -> int:
        return self.getMinInserts(s, 0, len(s) - 1, {})

    def getMinInserts(self, string, left, right, memo):
        if (left, right) in memo:
            return memo[(left, right)]
        if left >= right:
            return 0

        while left <= right and string[left] == string[right]:
            left += 1
            right -= 1
        if left <= right and string[left] != string[right]:
            memo[(left, right)] = min(self.getMinInserts(string, left + 1, right, memo), self.getMinInserts(string, left, right - 1, memo)) + 1
            return memo[(left, right)]
        else:
            return 0
    
