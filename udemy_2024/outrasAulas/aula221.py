class MinhaString(str):
    def upper(self):
        print('Meu upper')
        return super().upper()

ms = MinhaString('Teste')
print(ms.upper())