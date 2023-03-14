class Solution:
    # O(n) Space | O(n) Time, where n is length of ppid
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        # find child of each process
        # pid, ppid[index] -> pid of parent of process pid[index]
        # child of process ppid[index] = pid[index]
        # example child of process 3 = 1
        # child of process 0 = 3
        # child of process 5 = 10
        # child of process 3 = 5

        # create child graph of processes
        processes = {}
        for index in range(len(ppid)):
            parent = ppid[index]
            child = pid[index]
            if parent not in processes:
                processes[parent] = []
            processes[parent].append(child)

        ids = []
        self.explore(processes, kill, ids)
        return ids

    def explore(self, graph, node, ids):
        if node not in graph:
            ids.append(node)
            return
        ids.append(node)
        
        for child in graph[node]:
            self.explore(graph, child, ids)
