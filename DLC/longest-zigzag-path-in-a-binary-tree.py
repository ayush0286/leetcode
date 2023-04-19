# Leetcode https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree
# Notes: on each node, if the child direction is not part of currZigzag, a new zigzag is formed for this direction
# JIRA: https://sde2.atlassian.net/browse/UB-22

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(n) Time | O(1) Space, where n is total number of nodes in tree
class Solution:
    maxLength = 0     

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        if root.left is not None:
            self.traverse(root.left, 1, "right")
        if root.right is not None:
            self.traverse(root.right, 1, "left")
        return self.maxLength

    
    def traverse(self, node, currLength, direction):
        if direction == "left":
            if node.left is None:
                self.maxLength = max(self.maxLength, currLength)
            else:
                self.traverse(node.left, currLength + 1, "right")
            if node.right is not None:
                self.traverse(node.right, 1, "left")
        else:
            if node.right is None:
                self.maxLength = max(self.maxLength, currLength)
            else:
                self.traverse(node.right, currLength + 1, "left")
            if node.left is not None:
                self.traverse(node.left, 1, "right")
    
