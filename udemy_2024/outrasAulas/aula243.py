def adiciona_repr(cls):
    def meu_repr(self):
        nome_classe = self.__class__.__name__
        dict_classe = self.__dict__
        repr = f'{nome_classe}({dict_classe})'
        return repr
    cls.__repr__ = meu_repr
    return cls

@adiciona_repr
class Time():
    def __init__(self, nome):
        self._nome = nome

# Time = adiciona_repr(Time)
t1 = Time('Flamengo')
print(t1)        