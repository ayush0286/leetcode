class Solution:
    # O(n^2) Time | O(n^2) Space, where n is length of numRows
    def generate(self, numRows: int) -> List[List[int]]:
        # traverse with index 1 and while index == len(prev Row), print 1
        # go over the next row
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        allRows = [[1], [1, 1]]
        prevRow = [1, 1]
        currRow = None

        for row in range(numRows - 2):
            currRow = [1 for col in range(len(prevRow))]
            for index in range(1, len(currRow)):
                currRow[index] = prevRow[index] + prevRow[index - 1]
            currRow.append(1)
            prevRow = currRow
            allRows.append(currRow)
        
        return allRows
