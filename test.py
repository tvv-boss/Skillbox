A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
A7 = [i if i%2 else 0 for i in A1 if 2 < i < 8]

','.join(str(j**2) for j in range(10))


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