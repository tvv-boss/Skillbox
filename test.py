# TODO протестировать
import time, random, numpy as np
import pandas as pd
import matplotlib.pyplot as plt



A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
A7 = [i if i%2 else 0 for i in A1 if 2 < i < 8]

print(','.join(str(j**2) for j in range(10)))
print(A0)
print(A1)
print(A2)
print(A3)
print(A4)
print(A5)
print(A6)
print(A7)


def f1(lIn):
  l1 = sorted(lIn)
  l2 = [i for i in l1 if i < 0.5]
  return [i * i for i in l2]

def f2(lIn):
  l1 = [i for i in lIn if i < 0.5]
  l2 = sorted(l1)
  return [i * i for i in l2]


def f3(lIn):
  l1 = [i * i for i in lIn]
  l2 = sorted(l1)
  return [i for i in l2 if i < (0.5 * 0.5)]

AA = [random.randint(0,1) for i in range(1000000)]
your_list = list(np.random.randint(0,100,1000))
print(your_list)
start_time = time.time()
f1(AA)
print("--- %s seconds 1 ---" % (time.time() - start_time))

start_time = time.time()
f2(AA)
print("--- %s seconds 2 ---" % (time.time() - start_time))

start_time = time.time()
f3(AA)
print("--- %s seconds 3 ---" % (time.time() - start_time))