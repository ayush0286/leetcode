class Solution:
    # O(mn) Space, O(mn) Time, where m and n are lengths of words
    def minDistance(self, word1: str, word2: str) -> int:
        width = len(word1) + 1
        height = len(word2) + 1
        distanceMatrix = [[0 for col in range(width)] for row in range(height)]

        # base case, distance for empty string
        for col in range(width):
            distanceMatrix[0][col] = col
        for row in range(height):
            distanceMatrix[row][0] = row

        for row in range(1, height):
            for col in range(1, width):
                if word1[col - 1] == word2[row - 1]:
                    distanceMatrix[row][col] = distanceMatrix[row - 1][col - 1]
                else:
                    distanceMatrix[row][col] = 1 + self.getMinDistance(row, col, distanceMatrix)
        return distanceMatrix[-1][-1]


    def getMinDistance(self, row, col, matrix):
        return min(matrix[row - 1][col], matrix[row][col - 1], matrix[row - 1][col - 1])
