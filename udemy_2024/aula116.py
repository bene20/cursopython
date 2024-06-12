config={
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
}

def mostraargs(arg1, arg2, arg3):
    print(f'{arg1=}, {arg2=}, {arg3=}')

mostraargs(**config)