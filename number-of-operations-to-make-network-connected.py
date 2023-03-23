class Solution:
    
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # find out clusters
        # return clusters - 1 
        if len(connections) < n - 1:
            return -1
        
        graph = self.getGraph(n, connections)
        nodes = {}
        for node in range(n):
            nodes[node] = True

        clusterCount = self.getClusterCount(graph, nodes, n)
        return clusterCount - 1

    
    def getGraph(self, n, connections):
        graph = defaultdict(list)
        for connection in connections:
            start = connection[0]
            end = connection[1]
            graph[start].append(end)
            graph[end].append(start)
        return graph
    
    def explore(self, visited, graph, nodes, node):
        if node in visited or node not in nodes:
            return
        visited[node] = True
        del nodes[node]

        for neighbour in graph[node]:
            self.explore(visited, graph, nodes, neighbour)
        
        del visited[node]
    # O(n) Time | O(n) Space
    def getClusterCount(self, graph, nodes, n):
        clusterCount = 0
        for node in range(n):
            if node in nodes:
                self.explore({}, graph, nodes, node)
                clusterCount += 1
        return clusterCount
