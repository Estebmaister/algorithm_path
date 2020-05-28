# Copyright David Bai: Anyone can use this code without permission or referencing the original source
"""
Kosaraju Algorithm for graphs
List Based Iterative Implementation to find sizes of strongly connected components
Week 1 assignment for algorithm course 
"""

########################################################
# Data Structure Graph(v,e) with v € n and e € m

# node labels range from 1 to 875714. 875715 was used because of the range operator... range(875715) goes up to 875714.
init_node = 1
num_nodes = 875715  # n

# Adjacency representations of the graph and reverse graph
gr = [[] for i in range(num_nodes)]
r_gr = [[] for i in range(num_nodes)]

# The list index represents the node. If node i is unvisited then visited[i] == False and vice versa
visited = [False] * num_nodes

# The list below holds info about strongly connected components. The index is the scc leader and the value is the size of the scc.
scc = [0] * num_nodes

order = []  # The finishing orders after the first pass
stack = []  # Stack for DFS


########################################################
# Importing the graphs
# file_name = "test1.txt"  # Name of the test
file_name = "W1_SCC_Edges.txt"  # Name of the exam file
file = open(file_name, "r")
data = file.readlines()

for line in data:  # travel the list once to assign the edges to the graph O(m)
    items = line.split()
    gr[int(items[0])] += [int(items[1])]
    r_gr[int(items[1])] += [int(items[0])]

########################################################
# DFS-loop on reverse graph
for node in range(init_node, num_nodes):
    # Adding the node to the stack and marking it as visited
    if not visited[node]:
        visited[node] = True
        stack = [node]

    ## DFS(G,i)
    while stack:
        done = True  # Flag to know when DFS reach the further node
        for edge_node in r_gr[stack[-1]]:  # for each node stack[base_node] points at:
            # mark visited & push to stack if it hasn't been visited yet
            if not visited[edge_node]:
                visited[edge_node] = True
                stack.append(edge_node)
                done = False

        # if we don't find any unexplored nodes, the stack node is finished so we delete it & push it to order
        if done:
            order.append(stack.pop())


########################################################
# DFS on original graph
# print("order")
# print(order)
visited = [False] * len(visited)  # Resetting the visited variable
order.reverse()  # The nodes should be visited in reverse finishing times
# print("order reversed")
# print(order)
for node in order:
    # Adding the node to the stack and marking it as visited
    if not visited[node]:
        visited[node] = True
        stack = [node]

    ## DFS(G,i)
    while stack:
        done = True  # Flag to know when DFS reach the further node

        for edge_node in gr[stack[-1]]:  # for each node stack[base_node] points at:
            # mark visited & push to stack if it hasn't been visited yet
            if not visited[edge_node]:
                visited[edge_node] = True
                stack.append(edge_node)
                done = False

        # if we don't find any unexplored nodes, the stack node is finished so we delete it & push it to order
        if done:
            scc[stack[0]] += 1
            stack.pop()

########################################################
# Getting the five biggest sccs
# print("scc")
# print(scc)
scc.sort(reverse=True)
print("scc[:5]")
print(scc[:5])
