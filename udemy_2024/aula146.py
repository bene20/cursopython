generator=(n for n in range(10000))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print("=======================")

def gen1a10000():
    for n in range(10000):
        yield n
gen = gen1a10000()

print(next(gen))
print(next(gen))
print(next(gen))

print("=======================")
def meugenerator():
    yield 1
    yield 10
    yield 100
    yield 1000
    return 'FIM'

gen=meugenerator()
print(next(gen))
print(next(gen))
print(next(gen))
print("=======================")