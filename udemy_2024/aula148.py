
def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    yield from gen1()
    yield 10
    yield 20
    yield 30

gen = gen2()
for i in gen:
    print(i)

#print(next(gen))
#print(next(gen))

print("=======================")
