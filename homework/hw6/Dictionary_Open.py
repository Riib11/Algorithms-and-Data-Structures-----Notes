import math

class Entry:
    def __init__(self,key,value):
        self.key = key
        self.value = value

class BucketEntry(Entry):
    def __init__(self,key,value):
        Entry.__init__(self,key,value)
        self.next = None

class Dictionary:
    def __init__(self, capacity=5, threshold=0.8):
        self.makeTable(capacity)
        self.threshold = threshold

    def makeTable(self, capacity):
        # make sure capacity is prime
        while not is_prime(capacity): capacity += 1
        self.capacity = capacity
        self.slots = [None] * capacity
        self.size = 0

    def resize(self):
        old_table = self.slots
        self.makeTable(self.capacity * 2)
        
        for e in old_table:
            if e: self.insert(e.key,e.value)

    def insert(self,key,value):
        if self.size >= int(self.threshold * self.capacity): 
            self.resize()

        hs = hash(key)
        h1 = hs % self.capacity
        h2 = 1 + hs % (self.capacity - 1)
        h  = lambda t: (h1 + t*h2) % self.capacity

        i = h(0)
        t = 1
        while self.slots[i] != None:
            i, t = h(t), t+1

        self.slots[i] = Entry(key,value)
        self.size += 1

    def update(self,key,value):
        e = self.lookupHelp(key)
        if e is None:
            self.insert(key,value)
        else:
            e.value = value

    def lookupHelp(self,key):
        for slot in self.slots:
            if slot and slot.key == key: return slot
        return None

    def contains(self,key):
        return (self.lookupHelp(key) is not None)

    def lookup(self,key):
        e = self.lookupHelp(key)
        if e is None:
            raise KeyError
        return e.value
       
    # TODO 
    def delete(self,key):
        for i in range(self.capacity):
            e = self.slots[i]
            if e and e.key == key:
                # set targetted key to None
                self.slots[i] = None
                return

        # if not found
        raise KeyError

    def getSize(self):
        return self.size

    def asString(self):
        s = "{"
        first = False
        for slot in self.slots:
            if slot:
                first = True
                s += repr(slot.key) + ":" + repr(slot.value) + ", "
        if first: s = s[:-2]
        s += "}"
        return s

    def dump(self):
        for i in range(0,self.capacity):
            e = self.slots[i] 
            if e is None:
                print("  ["+str(i)+"]: None")
            else:
                print("  ["+str(i)+"]: ("+repr(e.key)+","+repr(e.value)+")")

    def iterate(self):
        keys = []
        for slot in self.slots:
            if slot: keys.append(slot.key)
        return iter(keys)

    __len__      = getSize
    __setitem__  = update
    __getitem__  = lookup
    __delitem__  = delete
    __contains__ = contains
    __repr__     = asString
    __str__      = asString
    __iter__     = iterate

def is_prime(x):
    for i in range(2,int(math.sqrt(x))):
        if x % i == 0: return False
    return True