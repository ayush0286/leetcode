class Solution:
    # O(log(mn)) Time | O(1) Space, where m and n are dimensions of matrix
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.findRow(matrix, target)
        if row is None:
            return False
        return self.binarySearch(matrix, row, target)


    def findRow(self, matrix, target):
        low = 0
        high = len(matrix) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == matrix[mid][-1]:
                return mid
            if target > matrix[mid][-1]:
                low = mid + 1
            else:
                if mid - 1 >= 0 and target <= matrix[mid - 1][-1]:
                    high = mid - 1
                else:
                    return mid
    

    def binarySearch(self, matrix, row, target):
        left = 0
        right = len(matrix[row]) - 1

        while left <= right:
            mid = (left + right) // 2
            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                left = mid + 1
            else:
                right = mid - 1
        return False
