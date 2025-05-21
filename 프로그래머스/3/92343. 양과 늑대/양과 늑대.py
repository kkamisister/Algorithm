from collections import defaultdict

def solution(info, edges):
    tree = defaultdict(list)
    for parent, child in edges:
        tree[parent].append(child)

    max_sheep = 0

    def dfs(current, sheep, wolf, visited):
        nonlocal max_sheep
        if info[current] == 0:
            sheep += 1
        else:
            wolf += 1

        if wolf >= sheep:
            return

        max_sheep = max(max_sheep, sheep)

        for i in range(len(visited)):
            if visited[i]:
                for child in tree[i]:
                    if not visited[child]:
                        visited_copy = visited[:]
                        visited_copy[child] = True
                        dfs(child, sheep, wolf, visited_copy)

    visited = [False] * len(info)
    visited[0] = True
    dfs(0, 0, 0, visited)

    return max_sheep
