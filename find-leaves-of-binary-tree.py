# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) Time | O(n) Space, where n is total nodes in tree
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodesAtDepths = defaultdict(list)
        maxDepth = self.traverse(root, nodesAtDepths)
        collectedLeaves = []
        for index in range(maxDepth + 1):
            collectedLeaves.append(nodesAtDepths[index])
        return collectedLeaves


    def traverse(self, node, nodesAtDepths):
        if node.left is None and node.right is None:
            nodesAtDepths[0].append(node.val)
            return 0
        left = 0
        right = 0
        if node.left is not None:
            left = self.traverse(node.left, nodesAtDepths)
        if node.right is not None:
            right = self.traverse(node.right, nodesAtDepths)
        currDepth = max(left, right) + 1
        nodesAtDepths[currDepth].append(node.val)
        return currDepth
