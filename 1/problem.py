from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n, edges):
        # Remove pass and write code here
        #build an adjaceny list
        graph = defaultdict(list)


        for edge in edges:
            [node1, node2] = edge
            graph[node1].append(node2)
            graph[node2].append(node1)

        print(graph)
        #run dfs on it
            