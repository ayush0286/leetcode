# Leetcode https://leetcode.com/problems/find-duplicate-subtrees
# Notes: optimize the brute force solution, by comparing the trees seperately, serialize trees and store in a hash
# JIRA: https://sde2.atlassian.net/browse/UB-17

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n^2) Time | O(n^2) Space, where n is total nodes in tree
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        hashset = defaultdict(list)
        self.serializeAllTrees(root, hashset)
        duplicates = []
        for key in hashset:
            print(key)
            if len(hashset[key]) > 1:
                duplicates.append(hashset[key][0])
        return duplicates
        
    def serializeAllTrees(self, node, hashset):
        if node is None:
            return
        key = self.serializeTree(node)
        hashset[key].append(node)
        self.serializeAllTrees(node.left, hashset)
        self.serializeAllTrees(node.right, hashset)
        

    def serializeTree(self, root):
        queue = deque([root])
        nodes = [str(root.val)]
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left is None:
                    nodes.append("null")
                else:
                    queue.append(node.left)
                    nodes.append(str(node.left.val))
                if node.right is None:
                    nodes.append("null")
                else:
                    queue.append(node.right)
                    nodes.append(str(node.right.val))
        return ','.join(nodes)
