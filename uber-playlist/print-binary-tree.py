# Leetcode https://leetcode.com/problems/print-binary-tree/
# Notes: how readable and modular is the code
# JIRA: https://sde2.atlassian.net/browse/UB-24

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(nlogn) Time | O(nlogn) Space, where n is total nodes in the tree
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        height = self.traverse(root) - 1
        rowLength = height + 1
        colLength = 2 ** (height + 1) - 1
        row = 0
        col = (colLength - 1 ) // 2
        childShift = 2 ** (height - row - 1)
        
        matrix = [["" for col in range(colLength)] for row in range(rowLength)]
        self.populateMatrix(matrix, row, col, root, height)
        return matrix
        
        
    def populateMatrix(self, matrix, row, col, node, height):
        if node is None:
            return
        matrix[row][col] = str(node.val)
        childShift = 2 ** (height - row - 1)
        row += 1
        self.populateMatrix(matrix, row, col - childShift, node.left, height)
        self.populateMatrix(matrix, row, col + childShift, node.right, height)
        
        
    def traverse(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        leftDepth = self.traverse(node.left)
        rightDepth = self.traverse(node.right)
        return max(leftDepth, rightDepth) + 1
        
