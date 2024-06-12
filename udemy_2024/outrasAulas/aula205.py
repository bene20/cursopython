class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome=sobrenome
        self.idade=idade

# p1 = Pessoa('Ana', 'Perez', 25)        
# print(f'Antes: {p1.__dict__}')
# del p1.sobrenome
# print(f'Depois: {p1.__dict__}')


p1 = Pessoa('Ana', 'Perez', 25)        
p1.__dict__['nome'] = 'Bia'
print(p1.__dict__)