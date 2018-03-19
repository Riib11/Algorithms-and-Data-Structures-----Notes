from Dictionary_Open import *

# initialize
d = Dictionary()
print("before insert   :",d)

# testing insert
i = 0
for v in "abcdefg":
    d[v] = i
    i += 1
print("after insert    :",d)

# testing updates
for k in "example":
    d[k] = 0
print("after updates   :",d)

# testing lookup
ls = []
for k in "abcdefg":
    ls.append(d[k])
print("lookup list     :",ls)

# testing delete
for k in [k for k in d]: # so it loads keys before modifying d
    if d[k] == 0:
        print(k)
        del d[k]
print("after deletes   :",d)

# testing dumo
print("dump:")
d.dump()

# testing load
d = Dictionary()
for i in range(1,1000):
    d[i] = i

total = sum([d[k] for k in d])
print("sum([1...1000]) :",total)