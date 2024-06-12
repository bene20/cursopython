class Casa:
    def __init__(self, cor):
        self._cor = cor

    def __metodo_privado(self):
        print('Acessei o método privado')

c1 = Casa('Verde')
c1._Casa__metodo_privado()
