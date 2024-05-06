from random import randint


class HashTable:
    def __init__(self, length):
        self.length = length
        self.table = [None] * self.length
        self.slots = [None] * self.length

    def __hash_function(self, value):
        return value % self.length

    def __rehash_function(self, value):
        return (value + 1) % self.length

    def __put(self, *args):
        self.slots[args[0]] = args[1]
        self.table[args[0]] = args[2]
        return None
        
    def __get(self, *args):
        return self.table[args[0]]

    def __delete(self, *args):
        self.slots[args[0]] = None
        self.table[args[0]] = None
        return None
        
    def __core(self, key, to, function, value=None):
        key_hash = self.__hash_function(key)
        if self.slots[key_hash] == to:
            return function(key_hash, key, value)
        else:
            c = 0
            while c != self.length:
                key_hash = self.__rehash_function(key_hash)
                if self.slots[key_hash] == to:
                    return function(key_hash, key, value)
                c += 1

    def put(self, key, value):
        self.__core(key=key, value=value, to=None, function=self.__put)

    def get(self, key):
        self.__core(key=key, to=key, function=self.__get)

    def delete(self, key):
        self.__core(key=key, to=key, function=self.__delete)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        self.delete(key)

    def in_(self, value):
        key = self.__hash_function(value)
        if self.table[key] == value:
            return True
        else:
            return False

    def __str__(self):
        return str(self.table)

    def __len__(self):
        return self.length


l = 20
hash_table = HashTable(l)

for _ in range(l):
    hash_table.put(key=randint(1, 100), value=randint(1, 1000))

print(hash_table)
print(len(hash_table))
