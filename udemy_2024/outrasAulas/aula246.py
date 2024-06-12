from typing import Any


class Decuplica:
    def __init__(self, funcDecorada):
        self._funcDecorada = funcDecorada

    def __call__(self, *args):
        return self._funcDecorada(*args) * 10

class Multiplica:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

    def __call__(self, funcaoDecorada):
        def interno(*args, **kwargs):
          return funcaoDecorada(*args, **kwargs) * self._multiplicador

        return interno

@Multiplica(5)
def soma(a, b):
    return a + b

print(soma(2,4))