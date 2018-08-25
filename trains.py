#!/usr/bin/env python3


from collections import deque


cat = ''.join


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
