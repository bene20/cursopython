def em_casa(metodo):
    def interno(self, *args, **kwargs):
        if self._nome == 'Terra':
            return 'Estou em casa'
        return metodo(self, *args, **kwargs)
    return interno

class Planeta:
    def __init__(self, nome):
        self._nome = nome

    @em_casa
    def falar_nome(self):
        return f'{self._nome}'
    
p1 = Planeta('Terra')
p2 = Planeta('Marte')

print(p1.falar_nome())
print(p2.falar_nome())