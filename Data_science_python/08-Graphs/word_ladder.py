from functools import lru_cache
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
        return set(self.connectedTo.keys())

    def getId(self):
        return self.id

    def getWeight(self, neighbor):
        return self.connectedTo[neighbor]

    def __str__(self):
        return str(self.id) + " connected to: " + str([nbr for nbr in self.connectedTo.keys()])


class Graph:
    def __init__(self):
        self.vertDict = {}
        self.lengthOfVert = 0

    def addVertix(self, key:int):
        self.lengthOfVert += 1
        newVert = Vertix(key)
        self.vertDict[key] = newVert        
        return newVert

    def addEdge(self, fromVertKey, toVertKey, weight = 0):
        if fromVertKey not in self.vertDict:
            self.addVertix(fromVertKey)

        if toVertKey not in self.vertDict:
            self.addVertix(toVertKey)

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

    def __addVertixList(self,word_list):
        for word in word_list:
            self.addVertix(word)

    def makeGraph(self):
        bucket = {}

        with open("08-Graphs/selected_four-letter_words.txt","r") as wordsf:
            words = wordsf.read().split("\n")
            self.__addVertixList(words)

        for word in words:
            for i in range(len(word)):
                d = word[:i] + "_" + word[i+1:]
                if d in bucket:
                    bucket[d].append(word)
                else:
                    bucket[d] = [word]

        for keys in bucket.keys():
            for word1 in bucket[keys]:
                for word2 in bucket[keys]:
                    if word1 != word2:
                        self.addEdge(word1,word2)
    @lru_cache
    def bfs(self, start, goal):
        queue = [(start, [start])]
        while queue:
            vertix, path = queue.pop(0)
            for next in self.getVertix(vertix).getConnections() - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    queue.append((next, path + [next]))

    def dfs(self, start):
        visited = set()
        adj = [start]
        while adj:
            vertix = adj.pop()
            if vertix not in visited:
                visited.add(vertix)
                adj.extend(self.getVertix(vertix).getConnections() - visited)
        return visited


gr = Graph()
gr.makeGraph()
# word_list = gr.bfs("yowl","aged")
# for _ in range(1):
    # print(next(word_list))
    # print()
list_ = gr.dfs("aahs")
print(sorted(list_))
