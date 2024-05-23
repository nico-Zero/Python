import pprint
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

    def getConnections(self) -> list:
        return list(self.connectedTo.keys())

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

        # pprint.pp(bucket)
    def __word_Letter_match(self, first, second):
        i = 0
        for f,s in zip(first,second):
            if f == s:
                i += 1
        return i 
    
    def word_ladder_search(self, start, end):
        if start == end:
            return start

        match_list = {}
        match_max = 0
        start = self.getVertix(start)
        if start is None:
            return None
        start_connections = start.getConnections()
        word_list = [start.getId()]

        while end not in word_list:
            for index,word in enumerate(start_connections):
                mat = self.__word_Letter_match(end, word)
                if mat >= match_max and word not in word_list:
                    match_list[mat] = index

            match_max = max(match_list)
            start = self.getVertix(start_connections[match_list[match_max]])
            word_list.append(start.getId())
            start_connections = start.getConnections()
            match_list.clear()
        return word_list

gr = Graph()
gr.makeGraph()
word_list = gr.word_ladder_search("zyme","aahs")
print(word_list)
