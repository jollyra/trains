#!/usr/bin/env python3


from collections import namedtuple


Edge = namedtuple('Edge', ['src', 'dest', 'weight'])


def parse_edge(string):
    return Edge(src=string[0], dest=string[1], weight=int(string[2:]))


def parse_edge_list(line):
    return [parse_edge(edge.strip()) for edge in line.split(',')]


if __name__ == '__main__':
    E = parse_edge_list('AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7')

    for e in E:
        print(e)
