from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque


# Counter
a = "aaaaaaaaaaaaahhhhhhrrrrr"
count = Counter(a)
print(count)
print(count.items())
print(count.keys())
print(count.values())
print(count.most_common(1)[0][0])
print(list(count.elements()))

# namedtuple
Point = namedtuple("Point", "x,y")
pt = Point(1, -5)
print(pt)

# OrderedDict
order_d = OrderedDict()  # this function remembers order.

order_d["b"] = 2
order_d["c"] = 3
order_d["a"] = 1
order_d["d"] = 4
order_d["e"] = 5

print(order_d)

# defaultdict
order_dif = defaultdict(int)

order_dif["b"] = 2
order_dif["c"] = 3
order_dif["a"] = 1
order_dif["d"] = 4
order_dif["e"] = 5

print(order_dif)

# deque

d = deque()

d.append(1)
d.append(2)
d.append(3)
d.append(4)
d.appendleft(5)
print(d)
d.pop()
print(d)
d.popleft()
print(d)
