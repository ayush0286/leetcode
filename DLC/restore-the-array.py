# Leetcode https://leetcode.com/problems/restore-the-array
# Notes: for each digit, either it can be part of existing chain, or it can form a new chain, 
#         traverse right to left, keeping track of possible array count till previous index, 
#         right to left traversal for handling 0 easily
# JIRA: https://sde2.atlassian.net/browse/UB-55

class Solution:
    # O(nk) Time | O(n) Space, where n is length of s and k is k // 10
    def numberOfArrays(self, s: str, k: int) -> int:
        modulo = 10 ** 9 + 7
        n = len(s)
        arrayCounts = [0] * (n + 1)
        arrayCounts[-1] = 1
        for index in reversed(range(n)):
            char = s[index]
            if char == '0':
                arrayCounts[index] = 0
            else:
                number = int(char)
                j = index + 1
                while j <= n and number <= k:
                    arrayCounts[index] += (arrayCounts[j] % modulo)
                    if j < n:
                        number = int(s[index: j + 1])
                    else:
                        break
                    j += 1
        return arrayCounts[0] % (10 ** 9 + 7)
