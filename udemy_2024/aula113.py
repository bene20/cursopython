
def multiplica(*args):
    total=1
    for num in args:
        total *= num
    return total

numeros=[2,3,5,8] #240

print(multiplica(*numeros))

print(multiplica(2,3,5,8))