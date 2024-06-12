def inc():
    x = 0
    def intinc():
        nonlocal x
        x += 1
        return x
    return intinc

x = inc()
print(x())
print(x())
print(x())
print("=========")
y = inc()
print(y())
print(y())
print(y())


