import sys
print('Estou no módulo', __name__)
print('sys.path é')
print(*sys.path, sep='\n')