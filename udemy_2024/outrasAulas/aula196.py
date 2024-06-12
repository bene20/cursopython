# def imprimir(a, b, /, c, d):
#     print(f'{a=}, {b=}, {c=}, {d=}')

# imprimir(1,2,3,4) # Válido
# imprimir(1,2,3,d=4) # Válido
# imprimir(1,2,c=3,d=4) # Válido
# imprimir(1,b=2,c=3,d=4) # Inválido

def imprimir(a, b, *, c, d):
    print(f'{a=}, {b=}, {c=}, {d=}')

imprimir(1,2,c=3,d=4) # Válido
imprimir(a=1,b=2,c=3,d=4) # Válido
# imprimir(1,2,3,4) # Inválido
# imprimir(1,2,3,d=4) # Inválido
# imprimir(1,b=2,c=3,d=4) # Inválido