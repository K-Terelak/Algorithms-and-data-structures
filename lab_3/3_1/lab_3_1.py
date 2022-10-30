from setuptools.namespaces import flatten


def find_min_spanning_tree(graph):
    vertices_count = len(graph)  # total vertices
    graph_max = max(flatten(graph))  # maximum edge
    vertices_found = [False] * vertices_count  # found vertices
    edges_found = 0  # found edges
    vertices_found[0] = True  # start from vertex 0
    minimum_spanning_tree = 0

    while edges_found < vertices_count - 1:  # find (vertices_count-1) edges
        minimum_edge = graph_max
        vertex_from = 0
        vertex_to = 0
        for i in range(vertices_count):
            if vertices_found[i]:
                for j in range(vertices_count):  # find minimum edge
                    if (not vertices_found[j]) and graph[i][j]:
                        if minimum_edge > graph[i][j]:
                            minimum_edge = graph[i][j]
                            vertex_from = i
                            vertex_to = j
        print("#", vertex_from, " - #", vertex_to, " distance: ", graph[vertex_from][vertex_to])
        vertices_found[vertex_to] = True
        minimum_spanning_tree += graph[vertex_from][vertex_to]
        edges_found += 1
    return minimum_spanning_tree


g = [
    [0, 0, 3, 0, 0],
    [0, 0, 10, 4, 0],
    [3, 10, 0, 2, 6],
    [0, 4, 2, 0, 1],
    [0, 0, 6, 1, 0],
]

print("Minimum spanning tree:", find_min_spanning_tree(g))  # 10
