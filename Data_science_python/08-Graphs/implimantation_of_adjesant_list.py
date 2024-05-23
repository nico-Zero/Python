class Vertix:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, neighbor, weight = 0):
        self.connectedTo[neighbor] = weight

    def removeNeighbor(self, key):
        for neighbor in self.connectedTo.keys():
            if neighbor.id == key:
                self.connectedTo.pop(neighbor)
                return None

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, neighbor):
        return self.connectedTo[neighbor]

    def __str__(self):
        return str(self.id) + " connected to: " + str([nbr.id for nbr in self.connectedTo.keys()])


class Graph:
    def __init__(self):
        self.vertDict = {}
        self.lengthOfVert = 0

    def addVertex(self, key:int):
        self.lengthOfVert += 1
        newVert = Vertix(key)
        self.vertDict[key] = newVert        
        return newVert

    def addEdge(self, fromVertKey, toVertKey, weight = 0):
        if fromVertKey not in self.vertDict:
            self.addVertex(fromVertKey)

        if toVertKey not in self.vertDict:
            self.addVertex(toVertKey)

        self.vertDict[fromVertKey].addNeighbor(toVertKey,weight) 

    def getVertix(self,key):
        if key in self.vertDict:
            return self.vertDict[key]
        else:
            return None

    def getVertices(self):
        return self.vertDict.values()

    def __iter__(self):
        return iter(self.vertDict.values())

    def __contains__(self,key):
        return key in self.vertDict

    def __str__(self):
        return str(self.getVertices())

def makeGraph(length):
    graph = Graph()
    for key in range(length):
        graph.addVertex(key)
    return graph

gr = makeGraph(20)

print(gr)
