class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome=sobrenome
        self.idade=idade

    @classmethod
    def criarSemNome(cls, idade):
        return cls('', '', 25)

    @staticmethod
    def meumetodo(x, y):
        return x+y

p1 = Pessoa('Ana', 'Perez', 20)
p2 = Pessoa.criarSemNome(25)
print('p1:', vars(p1))
print('p2:', vars(p2))

print(Pessoa.meumetodo(3,6))