def solution(inp):
    caves = [line.split('-') for line in inp.split('\n')]
    graph = {}
    for u, v in caves:
        graph[u] = graph.get(u, []) + [v]
        graph[v] = graph.get(v, []) + [u]
    
    return sum(depth_first('start', { 'start' }, graph, True))


def depth_first(u, path, graph, double):
    if u == 'end': 
        yield 1
    else: 
        for v in graph[u]:
            if v.islower():
                if v not in path:
                    yield from depth_first(v, path | { v }, graph, double)
                elif double and v not in ('start', 'end'):
                    yield from depth_first(v, path, graph, False)
            else: 
                yield from depth_first(v, path, graph, double)


raw = open('input.txt').read().rstrip()
print(solution(raw))