#!/usr/bin/env python3


def print_E(E):
    for edge, weight in E.items():
        print('{}: {}'.format(edge, weight))


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


if __name__ == '__main__':
    E = parse_E('AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7')
    print_E(E)

    assert weight(E, ['A', 'B', 'C']) == 9
    assert weight(E, ['A', 'D']) == 5
    assert weight(E, ['A', 'D', 'C']) == 13
    assert weight(E, ['A', 'E', 'B', 'C', 'D']) == 22
    assert weight(E, ['A', 'E', 'D']) is None
