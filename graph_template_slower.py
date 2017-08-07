#coding=utf-8


BFS = 1
DFS = 2


def traverse(graph, start, end, algorithm):
    path = []
    visited = [start]
    while visited:
        current = visited.pop(0)
        if current not in path:
            path.append(current)
            if current == end:
                return (True, path)
            if current not in graph:
                continue
        if algorithm == BFS:
            visited = extend_bfs_path(visited, graph[current])
        elif algorithm == DFS:
            visited = extend_dfs_path(visited, graph[current])
        else:
            raise ValueError("No such algorithm")
    return (False, path)


def extend_bfs_path(visited, current):
    return visited + current


def extend_dfs_path(visited, current):
    return current + visited