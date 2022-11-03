import sys


def show_result(distances):
    print("Vertex -> Distance")
    for index in range(len(distances)):
        print("#" + str(index), "->", distances[index])


# get the closest vertex, that is not already found
def get_closest_vertex_index(distances, already_found):
    minimum_distance = sys.maxsize

    for i in range(len(distances)):
        if distances[i] < minimum_distance and already_found[i] is False:
            minimum_distance = distances[i]
            min_index = i
    return min_index


def dijkstra(start_vertex, graph):
    distances = [sys.maxsize] * len(graph)  # initialize array with max distances
    distances[start_vertex] = 0  # distance to starting vertex(always 0)
    already_found = [False] * len(graph)  # already found vertices distance

    for _ in range(len(graph)):
        x = get_closest_vertex_index(distances, already_found)  # get the closest vertex

        already_found[x] = True

        # set distance
        for y in range(len(graph)):
            if graph[x][y] > 0 and already_found[y] is False and distances[y] > distances[x] + graph[x][y]:
                distances[y] = distances[x] + graph[x][y]

    show_result(distances)


g = [
    [0, 3, 1, 0, 0],
    [3, 0, 7, 5, 1],
    [1, 7, 0, 2, 0],
    [0, 5, 2, 0, 7],
    [0, 1, 0, 7, 0],
]
dijkstra(start_vertex=2, graph=g)
