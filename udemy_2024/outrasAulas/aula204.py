class MinhaClasse:
    meuAtributo='valor da classe'

    def __init__(self):
        self.meuAtributo = 'valor da instância'

    def getValorInstancia(self):
        return self.meuAtributo

    def getValorClasse(self):
        return MinhaClasse.meuAtributo
    

mc = MinhaClasse()

print('Valor da instância:', mc.getValorInstancia())
print('Valor da classe:', mc.getValorClasse())