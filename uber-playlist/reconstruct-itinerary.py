# Notes: sort end destinations in graph, create a counter for punched tickets, explore graph, modular code
# Leetcode: https://leetcode.com/problems/reconstruct-itinerary/
# JIRA: https://sde2.atlassian.net/browse/UB-13

class Solution:
# O(v + e) Time | O(v + e) Space, where v is vertices and e is edges of graph from tickets
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = self.getTicketGraph(tickets)
        counters = self.getTicketCounters(tickets)
        return self.explore("JFK", graph, counters, ["JFK"], len(tickets))
        
        
    def explore(self, airport, graph, counters, itineraries, ticketCount):
        if len(itineraries) == ticketCount + 1:
                return itineraries
            
        if airport not in graph:
            if len(itineraries) == ticketCount + 1:
                return itineraries
            else:
                return
            
        for neighbour in graph[airport]:
            key = self.getTicketKey([airport, neighbour])
            if counters[key] != 0:
                counters[key] -= 1
                itineraries.append(neighbour)
                itinerary = self.explore( neighbour, graph, counters, itineraries, ticketCount)
                if itinerary is not None:
                    return itinerary
                else:
                    itineraries.pop()
                counters[key] += 1
        return
        
        
    def getTicketGraph(self, tickets):
        graph = defaultdict(list)
        for ticket in tickets:
            start = ticket[0]
            end = ticket[1]
            graph[start].append(end)
        for key in graph:
            graph[key].sort()
        return graph
        
        
    def getTicketKey(self, ticket):
        return ticket[0] + ', ' + ticket[1]
    
    def getTicketCounters(self, tickets):
        ticketCounters = defaultdict(int)
        for ticket in tickets:
            key = self.getTicketKey(ticket)
            ticketCounters[key] += 1
        return ticketCounters
    
    
