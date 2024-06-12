class Veiculo():
    def exibe_info(self):
        print(self.__class__.__name__, ': Sou veículo')

class Aquatico(Veiculo):
    def exibe_info(self):
        print(self.__class__.__name__, ': Sou veículo aquático')

class Terrestre(Veiculo):
    def exibe_info(self):
        print(self.__class__.__name__, ': Sou veículo terrestre')

class Anfibio(Terrestre, Aquatico):
    ...
    
a1 = Anfibio()
a1.exibe_info()
print(*Anfibio.mro(), sep='\n')