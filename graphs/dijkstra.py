"""
Find the minimun path from node S to every other node in a graph
"""
import datetime

start = datetime.datetime.now()  # start timer for the process runtime

# The graph data must be in the format "node_init node_to_point,edge_long ... \n"
# the graph must have as many elements as rows are in the node_init column.

# Dijkstra algorithm O(m*n) (straightforward implementation)
def dijkstra(graph_dict, nodes_computed_dict):
    # If the source node isn't given, make the first node = source
    # with shortest path = 0 and add it to set X
    if not nodes_computed_dict:
        nodes_computed_dict = dict()
        nodes_computed_dict[1] = 0

    # Loop for finding the shortest path v -> w #with v € X & w € V-X
    while True:
        paths_per_node = dict()
        # creating paths_per_node, a dict with key: value -> (node_v, node_w): distance
        for node_v in nodes_computed_dict:
            for node_w_tuple in range(len(graph_dict[node_v])):
                if graph_dict[node_v][node_w_tuple][0] not in nodes_computed_dict:
                    paths_per_node[(node_v, graph_dict[node_v][node_w_tuple][0])] = (
                        graph_dict[node_v][node_w_tuple][1]
                        + nodes_computed_dict[node_v]
                    )

        # Extracting the shortest path, greedy criterion of dijkstra
        node_tuple = min(paths_per_node.items(), key=lambda x: x[1])

        # Adding vertex w (node_tuple[0][1]) to set X")
        nodes_computed_dict[node_tuple[0][1]] = node_tuple[1]

        if len(nodes_computed_dict) >= len(graph_dict):
            break

    return nodes_computed_dict


# Open the graph from data file_name and save it in a dictionary
# Graph format G(v,e) = G[node_v] -> [(node_x1,edge_long), (node_x2,edge_long), ...]

file_name = "dijkstraData.txt"
data_file = open(file_name, "r")
gr = dict()

for line in data_file:
    items = line.split()
    vertex = int(items[0])
    edges = [tuple(map(int, item.split(","))) for item in items][1:-1]
    gr[vertex] = gr.get(vertex, [])
    for edge in edges:
        gr[vertex] += [edge]
data_file.close()
# Set source vertex and call dijkstra function
# shortest_paths = dict()
# shortest_paths[1] = 0
set_sp = dijkstra(gr, dict())

# Record shortest-paths distances for demanded vertices
shortest_paths_req = []
req_nodes = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
for node in req_nodes:
    shortest_paths_req.append(set_sp.get(node, 1000000))

print("Shortest path for the required nodes:", shortest_paths_req)

end = datetime.datetime.now()
runtime = (end - start).microseconds * 1e-06  # total runtime in seconds
hours, remainder = divmod(runtime, (36 * 10 ** 8))  # hours in runtime, remaining secs
mins, secs = divmod(remainder, 6 * 10 ** 7)  # minutes and seconds in remainder
print("Runtime {:02.0f}:{:02.0f}:{:06.3f}".format(hours, mins, secs))
