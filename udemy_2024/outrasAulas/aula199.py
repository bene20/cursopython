class Pessoa():
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Ana', 'Perez')
p2 = Pessoa('Beto', 'Sanches')

print(f'{p1.nome=}, {p1.sobrenome=}')
print(f'{p2.nome=}, {p2.sobrenome=}')


class Carro():
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    def acelera(self):
        print(f'{self.modelo} acelerando')

c1 = Carro('Fusca', 1980)
c1.acelera()