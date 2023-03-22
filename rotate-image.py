class Solution:
    # O(n^2) Time | O(1) Space, where n is length of matrix 
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        quadRow = len(matrix) // 2
        isOdd = (len(matrix)) % 2 == 1
        quadCol = quadRow    
        row = 0
        col = 0
        for currRow in range(quadRow):
            if isOdd:
                quadCol = quadRow + 1
            for currCol in range(quadCol):
                turn = 0
                row = currRow
                col = currCol
                currElem = matrix[row][col]
                while turn < 4:
                    nextRow = col
                    nextCol = len(matrix) - 1 - row
                    nextElem = matrix[nextRow][nextCol]
                    matrix[nextRow][nextCol] = currElem
                    currElem = nextElem
                    turn += 1
                    row = nextRow
                    col = nextCol
