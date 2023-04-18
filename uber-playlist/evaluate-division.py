# Leetcode https://leetcode.com/problems/evaluate-division
# Notes: to evaluate unrelated variables, we need to hop from all intermediate variables
#        create a bidirectional graph for the same, and find target node
# JIRA: https://sde2.atlassian.net/browse/UB-16
# Time: ~ 2.5 hours (coded wrong solution, as finding out ancestors in graph)

class Solution:
    # O(v + e)n Time (O(v + e + n)) Space, where v and e are graph's vertices and edges
    # and n is length of queries 
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.createGraph(equations, values)
        solutions = []
        for query in queries:
            start = query[0]
            end = query[1]
            if start not in graph or end not in graph:
                solutions.append(float(-1))
                continue
            
            solution = self.findTarget(start, end, graph, {start: True}, float(1))
            if solution is None:
                solutions.append(float(-1))
            else:
                solutions.append(solution)
                
        return solutions
        
        
    def findTarget(self, node, target, graph, visited, product):
        if node == target:
            return product
        
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited[neighbour] = True
                newProduct = product * graph[node][neighbour]
                result = self.findTarget(neighbour, target, graph, visited, newProduct)
                if result is not None:
                    return result
                del visited[neighbour]          
        return
        
    
    def createGraph(self, equations, values):
        graph = defaultdict(dict)
        for i, equation in enumerate(equations):
            start = equation[0]
            end = equation[1]
            graph[start][end] = values[i]
            graph[end][start] = 1 / values[i]
        return graph
    
    
