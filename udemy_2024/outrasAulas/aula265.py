from dataclasses import dataclass, asdict, astuple

@dataclass
class Pessoa():
    nome: str
    idade: int

    # def __init__(self, nome: str, idade: int) -> None:
    #     self._nome = nome
    #     self._idade = idade

    # @property
    # def nome(self):
    #     return self._nome
    
    # @nome.setter
    # def nome(self, nome: str):
    #     self._nome = nome

    # @property
    # def idade(self):
    #     return self._idade
    
    # @idade.setter
    # def idade(self, idade: int):
    #     self._idade = idade

    # def __repr__(self) -> str:
    #     class_name = type(self).__name__
    #     attrs = f'(nome={self._nome!r}, idade={self._idade!r})'
    #     return f'{class_name}{attrs}'
    
p1 = Pessoa('Ana', 15)
print(p1, sep='\n')

print(asdict(p1))
print(astuple(p1))


from dataclasses import dataclass, field

@dataclass
class Pessoa2():
    nome: str = 'Pedro'
    idade: int = 17
    endenrecos: list[str] = field(default_factory=list)

p1 = Pessoa2()
print(p1, sep='\n')