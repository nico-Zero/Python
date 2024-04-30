from random import randint


# def generate_heap_list(l, difference):
#     heap_list = [0] + ([None] * (2**l))
#     l = 2 ** (l - 1)
#     r = 1
#     for i in range(1, l + randint(1, l + 1)):
#         heap_list[i] = randint(r, r + difference)
#         r += difference
#     return list(heap_list)


# heap_list = generate_heap_list(5, 15)
# for i, j in enumerate(heap_list):
#     print("{:<5}{:<5}".format(str(i), str(j)))


class binHeap:
    def __init__(self):
        self.heaplist = [0]
        self.currentSize = 0

    def __perUp(self, i):
        while i // 2 > 0:
            if self.heaplist[i] < self.heaplist[i // 2]:
                self.heaplist[i], self.heaplist[i // 2] = (
                    self.heaplist[i // 2],
                    self.heaplist[i],
                )
            i = i // 2

    def insert(self, key):
        self.heaplist.append(key)
        self.currentSize += 1
        self.__perUp(self.currentSize)

    def insertFromList(self, l):
        for key in l:
            self.heaplist.append(key)
            self.currentSize += 1

    def __perDown(self, i):
        while i * 2 <= self.currentSize:
            mc = self.findMin(i)
            if self.heaplist[i] > self.heaplist[mc]:
                self.heaplist[i], self.heaplist[mc] = (
                    self.heaplist[mc],
                    self.heaplist[i],
                )
            i = mc

    def findMin(self, i):
        if 1 * 2 + 1 > self.currentSize:
            return 1 * 2
        else:
            if self.heaplist[i * 2] < self.heaplist[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentSize]
        self.currentSize -= 1
        self.heaplist.pop()
        self.__perDown(1)
        return retval


x = binHeap()
for _ in range(10):
    x.insert(randint(1, 100))

print(x.heaplist)
x._binHeap__perUp(x.currentSize)  # type: ignore
print(x.heaplist)
