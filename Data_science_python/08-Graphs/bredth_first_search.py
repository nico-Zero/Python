from collections import OrderedDict
from enum import Enum
# import pprint

class State(Enum):
    unvisited = 1
    visited = 3
    visiting = 2

class Node:
    def __init__(self, id):
        self.id = id
        self.visit_state = State.unvisited
        self.adjacent = OrderedDict()

    def __str__(self):
        return str(self.id)

class Graph:
    def __init__(self) -> None:
        self.nodes = OrderedDict()

    def addNode(self, num):
        node = Node(num)
        self.nodes[num] = node
        return node
    def addEdge(self, source, dest, weight = 0):
        if source not in self.nodes:
            self.addNode(source)
        if dest not in self.nodes:
            self.addNode(dest)

        self.nodes[source].adjacent[self.nodes[dest]] = weight

