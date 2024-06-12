class CallMe:
    def __init__(self, number):
        self._number = number

    def __call__(self, nome):
        print(f'{nome} está chamando {self._number}')

c1 = CallMe('2345678')
c1('Pedro')