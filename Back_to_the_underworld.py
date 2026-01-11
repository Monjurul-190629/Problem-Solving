from collections import defaultdict, deque

def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = 0  # color 0
    count = [1, 0]  # count[0] for color 0, count[1] for color 1

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if v not in visited:
                visited[v] = 1 - visited[u]  # opposite color
                count[visited[v]] += 1
                queue.append(v)
    return max(count)

def solve():
    T = int(input())
    for case in range(1, T + 1):
        n = int(input())
        graph = defaultdict(list)
        nodes = set()

        for _ in range(n):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)
            nodes.add(u)
            nodes.add(v)

        visited = {}
        total = 0

        for node in nodes:
            if node not in visited:
                total += bfs(node, graph, visited)

        print(f"Case {case}: {total}")
