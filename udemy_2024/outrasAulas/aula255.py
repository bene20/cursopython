import enum

# Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])

class Direcoes(enum.Enum):
    ESQUERDA = 1
    DIREITA = 2

print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA)
print(Direcoes(1).name, Direcoes(1).value)