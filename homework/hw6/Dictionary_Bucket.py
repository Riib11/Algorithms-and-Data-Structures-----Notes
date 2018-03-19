
class Entry:
    def __init__(self,key,value):
        self.key = key
        self.value = value

class BucketEntry(Entry):
    def __init__(self,key,value):
        Entry.__init__(self,key,value)
        self.next = None

class Dictionary:
    def __init__(self, capacity=5, threshold=1.2):
        self.makeTable(capacity)
        self.threshold = threshold

    def makeTable(self, capacity):
        self.slots = [None] * capacity
        self.size = 0
        self.capacity = capacity

    def resize(self):
        old_table = self.slots
        self.makeTable(self.capacity * 2)

        for e in old_table:
            while e != None:
                self.insert(e.key,e.value)
                e = e.next

    def insert(self,key,value):
        if self.size >= int(self.threshold * self.capacity): 
            self.resize()

        i = hash(key) % self.capacity
        slot = self.slots[i]

        # already have bucket at index
        if slot:
            while slot.next != None: slot = slot.next
            slot.next = BucketEntry(key,value)

        # don't yet have bucket at index
        else:
            self.slots[i] = BucketEntry(key,value)
        
        self.size += 1

    def update(self,key,value):
        e = self.lookupHelp(key)
        if e is None:
            self.insert(key,value)
        else:
            e.value = value

    def lookupHelp(self,key):
        i = hash(key) % self.capacity
        slot = self.slots[i]

        # index has content
        if slot:
            # search through bucket
            while slot != None:
                if slot.key == key: return slot
                slot = slot.next
            # not found in bucket
            return None

        # index empty
        return None

    def contains(self,key):
        return (self.lookupHelp(key) is not None)

    def lookup(self,key):
        e = self.lookupHelp(key)
        if e is None:
            raise KeyError
        return e.value
    
    def delete(self,key):
        i = hash(key) % self.capacity
        prev = None
        curr = self.slots[i]

        if curr.key == key:
            self.slots[i] = curr.next
            return
        while curr != None:
            if curr.key == key:
                # remove curr from bucket
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

        # not found
        raise KeyError

    def getSize(self):
        return self.size

    def asString(self):
        s = "{"
        first = False
        for i in range(len(self.slots)):            
            e = self.slots[i]
            while e != None:
                first = True
                s += repr(e.key) + ":" + repr(e.value) + ", "
                e = e.next
            
        if first: s = s[:-2] # remove last comma
        s += "}"
        return s

    def dump(self):
        for i in range(0,self.capacity):
            e = self.slots[i] 
            if e is None:
                print("  ["+str(i)+"]: None")
            else:
                print("  ["+str(i)+"]:",end="")
                first = True
                while e != None:
                    if not first: print(" ->",end="")
                    print(" ("+repr(e.key)+","+repr(e.value)+")",end="")
                    first = False
                    e = e.next
                print()

    def iterate(self):
        keys = []
        for i in range(self.capacity):
            e = self.slots[i]
            while e != None:
                keys.append(e.key)
                e = e.next
        return iter(keys)

    __len__      = getSize
    __setitem__  = update
    __getitem__  = lookup
    __delitem__  = delete
    __contains__ = contains
    __repr__     = asString
    __str__      = asString
    __iter__     = iterate