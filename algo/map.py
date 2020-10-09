

def hash_humber(x):
    n = 1
    result = 13
    while x:
        result += n * (x % 10) ** n
        n += 1
        x = x // 10
    return result % 16


def hash_str(s):
    mask = (1 << 32) - 1
    h = 0
    for char in s:
        h = (h << 5 & mask) | (h >> 27)
        h += ord(char)
    return h


def hash_str(s):
    mask = (1 << 32) - 1
    h = 0
    for char in s:
        h += ord(char)
        h = h & mask
    return h



class MyBucket(object):

    def __init__(self):
        self.data = []

    def put(self, key, value):
        self.data.append((key, value))

    def get(self, key):
        for k, v in self.data:
            if k == key:
                return v
        raise KeyError()


class MyDict(object):
    def __init__(self):
        self.buckets = [MyBucket() for i in range(16)]
        self.size = 0

    def _hash(self, key):
        h = hash(key)
        return ((13*h + 31) % 127) % len(self.buckets)

    def put(self, key, value):
        h = self._hash(key)
        self.buckets[h].put(key, value)
        self.size += 1
        if self.size > len(self.buckets):
            self._rehash()

    def get(self, key):
        h = self._hash(key)
        self.buckets[h].get(key)

    def rehash(self):
        old_buckets = self.buckets
        self.buckets = [MyBucket() for i in range(self.size * 2)]
        for bucket in old_buckets:
            for k, v in bucket.data:
                self.put(k, v)
