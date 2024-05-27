# Collections: Counter, defaultdict, OrderedDict, namedtuple, deque
# Counter: A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
# defaultdict: A defaultdict will have a default value if that key has not been set yet.
# OrderedDict: An OrderedDict is a dictionary subclass that remembers the order in which its contents are added.
# namedtuple: A namedtuple is a container that stores values in fields, just like a class.
# deque: A deque is a double-ended queue. It can be used to add or remove elements from both ends.

# Counter
from collections import Counter

a = "aaaaabbbbcccdde"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())


# defaultdict
from collections import defaultdict

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['a'])
print(d['c'])

# OrderedDict
from collections import OrderedDict

d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
for k, v in d.items():
    print(k, v)

# namedtuple
from collections import namedtuple

Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

# deque
from collections import deque

d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)
d.pop()
print(d)