# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) Time | O(1) Space, where n is total nodes in tree
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        difference = float(inf)
        closest = root.val
        return self.traverse(root, difference, closest, target)

    def traverse(self, node, difference, closest, target):
        if node is None:
            return closest

        currDifference = abs(target - node.val)
        if currDifference < difference:
            difference = currDifference
            closest = node.val
        
        closest = self.traverse(node.left, difference, closest, target)
        closest = self.traverse(node.right, difference, closest, target)
        return closest
        
