
def restringe_param_string(funcao):
    def checa_params(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, str):
                raise TypeError(f'O argumento {arg} deve ser do tipo string!')
        return funcao(*args, **kwargs)
    return checa_params

@restringe_param_string
def invertestring(texto):
    return texto[::-1]

print(invertestring('meu texto')) # OK!
print(invertestring(321)) # Gera erro

# invertestring_checando_params = restringe_param_string(invertestring)
# print(invertestring_checando_params('texto checado'))
# print(invertestring_checando_params(321))