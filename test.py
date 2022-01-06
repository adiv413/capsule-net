import time
import random

t = [0 for i in range(10000)]
v = [0 for i in range(10000)]
x = time.time()
for i in range(10000):
    f = [t[j] * v[j] for j in range(10000)]
print(time.time() - x)


t = [random.random() for i in range(10000)]
v = [random.random() for i in range(10000)]

x = time.time()
for i in range(10000):
    f = [t[j] * v[j] for j in range(10000)]
print(time.time() - x)