from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from filho import Filho

class Pai:
    def __init__(self, nome: str, filho: 'Filho') -> None:
        self._nome = nome
        self._filho = filho

    def show_me(self):
        if self._filho is not None:
            print(f'Me chamo {self._nome} e sou pai de {self._filho._nome}')
        else:
            print(f'Me chamo {self._nome} e não tenho filho')