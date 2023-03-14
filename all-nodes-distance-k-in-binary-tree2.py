# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # O(n) Time | O(n) Space, where n is number of nodes in binary tree
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = {}
        self.getAdjacencyList(root, graph)

        nodeValues = []
        self.explore(graph, target, {}, nodeValues, 0, k)
        return nodeValues

        

    def explore(self, graph, node, visited, nodeValues, distance, k):
        visited[node] = True
        if distance == k:
            nodeValues.append(node.val)
            return nodeValues

        for neighbour in graph[node]:
            if neighbour not in visited:
                self.explore(graph, neighbour, visited, nodeValues, distance + 1, k)
        visited[node] = False
        return nodeValues

    def getAdjacencyList(self, node, graph):
        if node not in graph:
            graph[node] = []
        if node.left:
            graph[node].append(node.left)
            if node.left not in graph:
                graph[node.left] = []
            graph[node.left].append(node)
            self.getAdjacencyList(node.left, graph)
        if node.right:
            graph[node].append(node.right)
            if node.right not in graph:
                graph[node.right] = []
            graph[node.right].append(node)
            self.getAdjacencyList(node.right, graph)

