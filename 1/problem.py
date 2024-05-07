from collections import defaultdict, deque

class Solution:
    def countCompleteComponents(self, n, edges):
        #build an adjaceny list
        adj_list = defaultdict(list)
        graph_group = defaultdict(set)

        #groups are defined like islands(connections of nodes)
        #find the number of separated groups by using bfs and what nodes are a part of each group
            #a dictionary called graph group will hold one master node(key) and the nodes in that particular group, including itself(values)
        
        #iterate through the groups
            #if there is only 1 node in that group it doesn't need neighbors
            #if there is only 2 nodes in that group then every node in that group only needs 1 neighbor
            #if there is 3 or more node in that group than each node needs to have 2 neighbors
            #from each different group find if the node has the needed amt of neighbors 
                #if it doesn't then it isn't completed and we subtract 1
        
        visited = set()
        for edge in edges:
            [node1, node2] = edge
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)

        def _bfs(node):
            queue = deque([node])

            while len(queue):
                curr_node = queue.popleft()
                visited.add(curr_node)
                graph_group[node].add(curr_node)

                for neigh in adj_list[curr_node]:
                    if neigh not in visited:
                        queue.append(neigh) 
                
        num_of_groups = 0
        num_of_incomplete_groups = 0

        #finds # of groups and what nodes are associated in each group
        for i in range(n):
            if i not in visited:
                _bfs(i)
                num_of_groups +=1

        #helper function to return a boolean if it is a completed graph
        def _is_not_a_complete_graph(master_node):
            amt_of_nodes_in_grp = len(graph_group[master_node])
            required_neighbor = 0
            if amt_of_nodes_in_grp <=1:
                required_neighbor = 0
            elif amt_of_nodes_in_grp == 2:
                required_neighbor = 1
            else:
                required_neighbor = 2
            for node in graph_group[master_node]:
                amt_of_neighbor_node = len(adj_list[node])
                if amt_of_neighbor_node != required_neighbor:
                    return True
            return False

        for master_node in graph_group:
            if _is_not_a_complete_graph(master_node):
                num_of_incomplete_groups +=1
        
        return num_of_groups - num_of_incomplete_groups




            