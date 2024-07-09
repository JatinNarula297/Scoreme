#!/usr/bin/env python
# coding: utf-8

# In[2]:


def longest_path(graph: list) -> int:
    def topological_sort(graph):
        n = len(graph)
        indegree = [0] * n
        for i in range(n):
            for j, _ in graph[i]:
                indegree[j] += 1
                
        stack = [i for i in range(n) if indegree[i] == 0]
        topo_order = []
        
        while stack:
            node = stack.pop()
            topo_order.append(node)
            for neighbor, _ in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    stack.append(neighbor)
        
        return topo_order

    def calculate_longest_path(graph, topo_order):
        n = len(graph)
        dist = [-float('inf')] * n
        
        for node in topo_order:
            if dist[node] == -float('inf'):
                dist[node] = 0
            for neighbor, weight in graph[node]:
                if dist[neighbor] < dist[node] + weight:
                    dist[neighbor] = dist[node] + weight
        
        return max(dist)
    
    topo_order = topological_sort(graph)
    return calculate_longest_path(graph, topo_order)

# Example usage:
graph = [
    [(1, 3), (2, 2)],
    [(3, 4)],
    [(3, 1)],
    []
]
print(longest_path(graph))

#output =7


# In[ ]:




