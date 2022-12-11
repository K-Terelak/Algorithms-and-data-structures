import math


def floyd_warshall(graph):
    vertices = len(graph)
    for r in range(vertices):
        for p in range(vertices):
            for q in range(vertices):
                graph[p][q] = min(graph[p][q], graph[p][r] + graph[r][q])
    print_result(graph=graph, vertices=vertices)


def print_result(graph, vertices):
    for p in range(vertices):
        for q in range(vertices):
            if graph[p][q] == math.inf:
                print("∞", end=" ")
            else:
                print(graph[p][q], end="  ")
        print(" ")


g = [
    [0, 5, math.inf, math.inf],
    [50, 0, 15, 5],
    [30, math.inf, 0, 15],
    [15, 40, 5, 0]
]
floyd_warshall(graph=g)
