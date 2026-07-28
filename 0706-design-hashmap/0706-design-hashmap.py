class MyHashMap:

    def __init__(self):
        self.size = 1009
        self.map = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key, value):
        b = self.map[self._hash(key)]
        for i, (k, _) in enumerate(b):
            if k == key:
                b[i] = (key, value)
                return
        b.append((key, value))

    def get(self, key):
        b = self.map[self._hash(key)]
        for k, v in b:
            if k == key:
                return v
        return -1

    def remove(self, key):
        b = self.map[self._hash(key)]
        for i, (k, _) in enumerate(b):
            if k == key:
                b.pop(i)
                return