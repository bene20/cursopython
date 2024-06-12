class Ponto:
    def __init__(self, x:int, y:int, nome: str) -> None:
        self._x = x
        self._y = y
        self._nome = nome
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(x={self._x!r}, y={self._y!r}, nome={self._nome!r})'

p1 = Ponto(5,7,'Início')
p2 = Ponto(3,8,'Final')

print(p1,p2, sep='\n')