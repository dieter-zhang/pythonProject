# collections : Counter

from collections import Counter

a = "aaaaaabbcccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.values())
print(my_counter.most_common(1))
print(my_counter.most_common(2)[0][0])

# different elements
print(list(my_counter.elements()))

# ------
from collections import namedtuple

# create a class like structure
point = namedtuple('Point', 'x, y')
pt = point(1, -4)
print(pt)
print(pt.x, pt.y)

# ---
# remeber the order the element added
from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 1
ordered_dict['c'] = 1
ordered_dict['d'] = 1
ordered_dict['e'] = 1

print(ordered_dict)

# ---
from collections import defaultdict
d = defaultdict(list)
d['a'] = 1
d['b'] = 2
print(d['c'])

# ---
from collections import deque
d = deque()
d.append(1)
d.append(2)

d.appendleft(3)
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.extendleft([4,5,6])
print(d)
d.rotate(1)
print(d)