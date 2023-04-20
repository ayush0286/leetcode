# Leetcode https://leetcode.com/problems/maximum-width-of-binary-tree/
# Notes: calculate width by labeling each node with it's complete binary tree counterpart
# JIRA: https://sde2.atlassian.net/browse/UB-30

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) Time | O(n) Space, where n is total nodes in tree
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 1)]) # node, overall index
        maxWidth = 0
        while queue:
            width = queue[-1][1] - queue[0][1] + 1
            maxWidth = max(width, maxWidth)
            for elem in range(len(queue)):
                node, index = queue.popleft()

                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))
        return maxWidth
