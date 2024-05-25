x=1

def minhafunc1():
  x=10
  print(f'minhafunc1: {x=}')

def minhafunc2():
  global x
  x=10
  print(f'minhafunc2: {x=}')

print(f'fora 1: {x=}')
minhafunc1()
print(f'fora 2: {x=}')
minhafunc2()
print(f'fora 3: {x=}')