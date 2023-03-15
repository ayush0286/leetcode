# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) Time | O(n) Space, where n is number of nodes in tree
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        lefts = []
        rights = []
        leftLeaves = []
        rightLeaves = []
        boundary = [root.val]
        if root.left is not None:
            self.leftTraversal(root.left, True, lefts, leftLeaves)
        boundary.extend(lefts)
        boundary.extend(leftLeaves)
        if root.right is not None:
            self.rightTraversal(root.right, True, rights, rightLeaves)
        for node in reversed(rightLeaves):
            boundary.append(node)
        for node in reversed(rights):
            boundary.append(node)
        return boundary

    def leftTraversal(self, node, leftPossible, lefts, leftLeaves):
        if node is None:
            return

        if leftPossible:
            if node.left is None and node.right is None:
                leftLeaves.append(node.val)
                leftPossible = False
                return
            
            lefts.append(node.val)
            if node.left is not None:
                self.leftTraversal(node.left, True, lefts, leftLeaves)
            
            if node.right is None:
                return
            if node.left is None:
                self.leftTraversal(node.right, True, lefts, leftLeaves)
            else:
                self.leftTraversal(node.right, False, lefts, leftLeaves)
        
        else:
            if node.left is None and node.right is None:
                leftLeaves.append(node.val)
                return
            
            self.leftTraversal(node.left, False, lefts, leftLeaves)
            self.leftTraversal(node.right, False, lefts, leftLeaves)
    
    def rightTraversal(self, node, rightPossible, rights, rightLeaves):
        if node is None:
            return 
        if rightPossible:
            if node.left is None and node.right is None:
                rightLeaves.append(node.val)
                rightPossible = False
                return

            rights.append(node.val)
            if node.right is not None:
                self.rightTraversal(node.right, True, rights, rightLeaves)

            if node.left is None:
                return
            
            if node.right is None:
                self.rightTraversal(node.left, True, rights, rightLeaves)
            else:
                self.rightTraversal(node.left, False, rights, rightLeaves)
        else:
            if node.right is None and node.left is None:
                rightLeaves.append(node.val)
                return
            
            self.rightTraversal(node.right, False, rights, rightLeaves)
            self.rightTraversal(node.left, False, rights, rightLeaves)
