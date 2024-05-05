from random import randint


class HashTable:
    def __init__(self, length):
        self.length = length
        self.table = [None] * self.length

    def __hash_function(self, value):
        return value % self.length

    def put(self, value):
        key = self.__hash_function(value)
        if self.table[key] is None:
            self.table[key] = value
            return None
        else:
            for new_key in range(self.length):
                if self.table[new_key] is None:
                    self.table[new_key] = value
                    return None
                else:
                    continue
        raise ValueError("There table is full !")

    def get(self, key):
        return self.table[key]

    def delete(self, key):
        if 0 <= key < self.length:
            self.table[key] = None
        else:
            raise ValueError("Invalid Kye value.")

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
    hash_table.put(randint(1, 1000))

print(hash_table)
print(len(hash_table))
