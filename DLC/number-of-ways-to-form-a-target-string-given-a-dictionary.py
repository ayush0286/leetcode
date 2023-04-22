# Leetcode https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary
# Notes: what states will help us solve the subproblem at ith target and kth word index in words
# JIRA: https://sde2.atlassian.net/browse/UB-37

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        grid = [[0 for col in range(len(words[0]) + 1)] for row in range(len(target) + 1)]

        for col in range(len(grid[0])):
            grid[0][col] = 1

        charCounts = defaultdict(int)

        for index in range(len(words[0])):
            for word in words:
                char = word[index]
                charCounts[(char, index)] += 1
        
        for row in range(1, len(grid)):
            for col in range(1, len(grid[row])):
                char = target[row - 1]
                charCount = charCounts[(char, col - 1)]
                # charCount = self.getCharCount(words, char, col - 1)

                grid[row][col] = charCount * grid[row - 1][col - 1] + grid[row][col - 1]
        return grid[-1][-1] % (10 ** 9 + 7)

    def getCharCount(self, words, char, index):
        charCount = 0
        for word in words: 
           if word[index] == char:
               charCount += 1
        return charCount
