class Casa:
    def __init__(self, cor):
        self._cor = cor

    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        self._cor = valor

c1 = Casa('Verde')    
print(c1.cor)
c1.cor = 'Amarelo'
print(c1.cor)
