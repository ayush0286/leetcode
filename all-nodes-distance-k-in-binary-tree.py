# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        nodeValues = []
        # find target node, keeping track of parents
        parentNodes = self.parentNodes(root, target, [])

        # for each parent node run k - 1 and add those
        for index in reversed(range(len(parentNodes))):
            if k == 0:
                nodeValues.append(parentNodes[index]["node"].val)
                return nodeValues
            currentNodeValues = []
            
            if parentNodes[index]["direction"] == "left":
                self.nodesAtDistanceK(parentNodes[index]["node"].right, k - 1, currentNodeValues)
            elif parentNodes[index]["direction"] == "right":
                self.nodesAtDistanceK(parentNodes[index]["node"].left, k - 1, currentNodeValues)
            else:
                self.nodesAtDistanceK(parentNodes[index]["node"], k, currentNodeValues)
            nodeValues.extend(currentNodeValues)
            k -= 1
        return nodeValues


    def nodesAtDistanceK(self, node, k, nodes):
        if node == None:
            return 

        if k == 0:
            nodes.append(node.val)
            return

        self.nodesAtDistanceK(node.left, k - 1, nodes)
        self.nodesAtDistanceK(node.right, k - 1, nodes)
        return 

    def parentNodes(self, root: TreeNode, target: TreeNode, parentNodesList: List[TreeNode]) -> List[TreeNode]:
        if root == None:
            return parentNodesList

        if root.val == target.val:
            parentNodesList.append({"node": root, "direction": None})            
            return parentNodesList
        
        parentNodesList.append({"node": root, "direction": "left"})
        parentNodesList = self.parentNodes(root.left, target, parentNodesList)
        if parentNodesList[-1]["node"] == target:
            return parentNodesList
        parentNodesList.pop()
        parentNodesList.append({"node": root, "direction": "right"})
        parentNodesList = self.parentNodes(root.right, target, parentNodesList)
        if parentNodesList[-1]["node"] == target:
            return parentNodesList
        parentNodesList.pop()   
        return parentNodesList


        
