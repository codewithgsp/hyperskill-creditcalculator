
from math import log

x, y = map(int, [input(), input()])
if y < 1:
    print(round(log(x), 2))
else:
    print(round(log(x, y), 2))
