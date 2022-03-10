import heapq

def solution(inp):
    maze = [list(map(int, line)) for line in inp.split('\n')]
    fullmaze = []
    for i in maze:
        line = i
        prev = i
        for _ in range(4):
            prev = [x + 1 if x + 1 < 10 else 1 for x in prev]
            line.extend(prev)
        fullmaze.append(line)

    temp = fullmaze.copy()
    for _ in range(4):
        prev = []
        for i in temp:
            prev.append([x + 1 if x + 1 < 10 else 1 for x in i])
        fullmaze.extend(prev)
        temp = prev.copy()
    maze = fullmaze.copy()

    graph = {}
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            neighbours = {}
            if y > 0:
                neighbours[(((y - 1) * len(maze[0])) + x)] = maze[y - 1][x]
            if x > 0:
                neighbours[((y * len(maze[0])) + (x - 1))] = maze[y][x - 1]
            if y < len(maze) - 1:
                neighbours[(((y + 1) * len(maze[0])) + x)] = maze[y + 1][x]
            if x < len(maze[0]) - 1:
                neighbours[((y * len(maze[0])) + (x + 1))] = maze[y][x + 1]

            graph[((y * len(maze[0])) + x)] = neighbours

    shortest = dijkstra(graph, 0)[len(maze[0]) * len(maze) - 1]
    return shortest


def dijkstra(graph, starting):
    dist = { vertex: float('inf') for vertex in graph }
    dist[starting] = 0

    q = [(0, starting)]
    while len(q) > 0:
        u_d, u = heapq.heappop(q)

        if u_d > dist[u]:
            continue

        for v, weight in graph[u].items():
            new_d = u_d + weight

            if new_d < dist[v]:
                dist[v] = new_d
                heapq.heappush(q, (new_d, v))

    return dist


raw = open('input.txt').read().rstrip()
print(solution(raw))