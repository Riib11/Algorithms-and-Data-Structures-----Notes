
class Entry:
    def __init__(self,key,value):
        self.key = key
        self.value = value

class BucketEntry(Entry):
    def __init__(self,key,value):
        Entry.__init__(self,key,value)
        self.next = None

class Dictionary:
    def __init__(self, capacity=5, threshold=1):
        self.makeTable(capacity)
        self.threshold = threshold

    def makeTable(self, capacity):
        self.slots = [None] * capacity
        self.size = 0
        self.capacity = capacity

    def resize(self):
        old_size     = self.size
        old_capacity = self.capacity
        old_table    = self.slots

        self.makeTable(self.capacity * 2)

        for i in range(0,old_size):
            e = old_table[i]
            self.insert(e.key,e.value)

    def insert(self,key,value):
        if self.size >= int(self.threshold * self.capacity): 
            self.resize()
        self.slots[self.size] = Entry(key,value)
        self.size += 1

    def update(self,key,value):
        e = self.lookupHelp(key)
        if e is None:
            self.insert(key,value)
        else:
            e.value = value

    def lookupHelp(self,key):
        for i in range(0,self.size):
            if self.slots[i].key == key:
                return self.slots[i]
        return None

    def contains(self,key):
        return (self.lookupHelp(key) is not None)

    def lookup(self,key):
        e = self.lookupHelp(key)
        if e is None:
            raise KeyError
        return e.value
        
    def delete(self,key):
        i = 0
        while i < self.size and self.slots[i].key != key:
            i += 1
        if i == self.size:
            return
        self.size -= 1
        while i < self.size:
            self.slots[i] = self.slots[i+1]
            i += 1

    def getSize(self):
        return self.size

    def asString(self):
        s = "{"
        first = True
        for i in range(0,self.size):
            if not first:
                s += ","
            e = self.slots[i] 
            s += repr(e.key) + ":" + repr(e.value)
            first = False
        s += "}"
        return s

    def dump(self):
        for i in range(0,self.capacity):
            e = self.slots[i] 
            if e is None:
                print("["+str(i)+"]: None")
            else:
                print("["+str(i)+"]: ("+repr(e.key)+","+repr(e.value)+")")

    __len__      = getSize
    __setitem__  = update
    __getitem__  = lookup
    __delitem__  = delete
    __contains__ = contains
    __repr__     = asString
    __str__      = asString
