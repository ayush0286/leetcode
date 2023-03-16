# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(max(n, m)) Time | O(1) Space, where n, m are number of nodes in trees respectively
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        isSame = self.traverseTogether(p, q)
        return True if isSame is None else False



    def traverseTogether(self, node1, node2):
        if node1 is None and node2 is not None:
            return False
        if node1 is not None and node2 is None:
            return False
        if node1 is None and node2 is None:
            return
        # has left child
        if node1.left is None and node2.left is not None:
            return False
        if node1.left is not None and node2.left is None:
            return False
        # has right child
        if node1.right is None and node2.right is not None:
            return False
        if node1.right is not None and node2.right is None:
            return False
        # has same val
        if node1.val != node2.val:
            return False

        alarm = None
        if node1.left is not None:
            alarm = self.traverseTogether(node1.left, node2.left)
        if alarm is not None and not alarm:
            return False
        
        if node1.right is not None:
            alarm = self.traverseTogether(node1.right, node2.right)
        if alarm is not None and not alarm:
            return False


