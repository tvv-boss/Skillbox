num = int(input())

def fib(n):

  if n <= 1:
    return 1
  else:
#    print(fib(n-1) + fib(n-2))
    return fib(n-1) + fib(n-2)

fib(num)






