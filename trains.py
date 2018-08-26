#!/usr/bin/env python3


from collections import deque, defaultdict
from heapq import heappush, heappop


cat = ''.join
BIG = 10 ** 999


def trace(func):
    def inner(*args, **kwargs):
        ret = func(*args, **kwargs)
        print('func: {}\targs: {}\tkwargs: {}\tret: {}'
              .format(func.__name__, args, kwargs, ret))
        return ret
    return inner


def print_E(E):
    for (src, dest), weight in E.items():
        print('{}->{}: {}'.format(src, dest, weight))


def parse_E(line):
    E = {}
    for edge in line.split(','):
        edge = edge.strip()
        E[(edge[0], edge[1])] = int(edge[2:])
    return E


def weight(E, path):
    weight = 0
    for i in range(len(path) - 1):
        e = (path[i], path[i + 1])
        if e in E:
            weight += E[e]
        else:
            return None
    return weight


def bfs_paths(E, src, dest, max_depth, min_depth=1):
    """ return all possible paths in graph E from src to dest with min_depth < depth < max_depth """
    paths = []
    horizon = deque([[src]])
    while horizon:
        path = horizon.popleft()
        v = path[-1]
        if v == dest and len(path) > min_depth:
            paths.append(path)
        if len(path) <= max_depth:
            for e in E:
                if e[0] == v:
                    horizon.append(path + [e[1]])
    return paths


def resolve_path(prev, v):
    if v is None:
        return []
    else:
        return resolve_path(prev, prev[v]) + [v]


def dijkstras_search(E, src, dest):
    cost = defaultdict(lambda: BIG)
    cost[src] = 0
    prev = {src: None}
    horizon = [(0, src)]
    while horizon:
        (u_cost, u) = heappop(horizon)
        if u == dest:
            return dict(cost=cost[dest], path=resolve_path(prev, dest))
        for edge in [edge for edge in E if edge[0] == u]:
            if cost[edge[0]] + E[edge] < cost[edge[1]]:
                heappush(horizon, (cost[edge[0]] + E[edge], edge[1]))
                cost[edge[1]] = cost[edge[0]] + E[edge]
                prev[edge[1]] = edge[0]
    return None


if __name__ == '__main__':
    E = parse_E('AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7')
    print_E(E)

    # Exercises 1-5
    assert weight(E, ['A', 'B', 'C']) == 9
    assert weight(E, ['A', 'D']) == 5
    assert weight(E, ['A', 'D', 'C']) == 13
    assert weight(E, ['A', 'E', 'B', 'C', 'D']) == 22
    assert weight(E, ['A', 'E', 'D']) is None

    # Exercise 6
    paths = bfs_paths(E, 'C', 'C', 3)
    assert len(paths) == 2
    print('paths from C to C where depth <= 3: {}'.format([cat(path) for path in paths]))

    # Exercise 7
    paths = bfs_paths(E, 'A', 'C', 4, min_depth=4)
    assert len(paths) == 3
    print('paths from A to C where depth is 4: {}'.format([cat(path) for path in paths]))

    # Exercise 8
    print(dijkstras_search(E, 'A', 'C'))

    # Exercise 9
    print(dijkstras_search(E, 'B', 'B'))

    E = parse_E('AB4, AC2, BC3, CB1, BD2, BE3, CD4, CE5, ED1')
    print(dijkstras_search(E, 'A', 'D'))
