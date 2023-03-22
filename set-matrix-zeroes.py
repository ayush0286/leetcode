class Solution:
    # O(nm) Time | O(1) Space, where n, m are dimensions of matrix
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        isFirstColumnZero = False

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    if col == 0:
                        isFirstColumnZero = True
                    else:
                        matrix[0][col] = 0
                    matrix[row][0] = 0
        
        for row in reversed(range(len(matrix))):
            for col in reversed(range(1, len(matrix[0]))):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        if isFirstColumnZero:
            for row in range(len(matrix)):
                matrix[row][0] = 0
        
