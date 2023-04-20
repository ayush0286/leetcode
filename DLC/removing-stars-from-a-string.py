# Leetcode https://leetcode.com/problems/removing-stars-from-a-string
# Notes: traverse string from right to left while counting * encountered on the way 
# JIRA: https://sde2.atlassian.net/browse/UB-35

class Solution:
    # O(n) Time | O(n) Space, where n is length of string
    def removeStars(self, s: str) -> str:
        count = 0
        reversedChars = []
        for index in reversed(range(len(s))):
            char = s[index]
            if char != '*' and count != 0:
                count -= 1
            elif char == '*':
                count += 1
            else:
                reversedChars.append(char)
        return ''.join(reversed(reversedChars))
