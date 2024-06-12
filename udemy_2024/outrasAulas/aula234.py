a : bool = False
a = 'oi'
print(f'{a=}')

class OutroError(Exception): ...

try:
    var = 1/0
except ZeroDivisionError as error:
    outraexcecao = OutroError('Alguma ação aqui')
    raise outraexcecao from error

