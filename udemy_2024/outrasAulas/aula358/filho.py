from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pai import Pai

class Filho:
    def __init__(self, nome: str, pai: 'Pai') -> None:
        self._nome = nome
        self._pai = pai

    def show_me(self):
        if self._pai is not None:
            print(f'Me chamo {self._nome} e sou filho de {self._pai._nome}')
        else:
            print(f'Me chamo {self._nome} e não tenho pai')        