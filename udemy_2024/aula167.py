
def fabrica_decorator(mensagem):
    def restringe_param_string(funcao):
        def inner(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, str):
                    tipoarg=type(arg)
                    raise TypeError(f'{arg} deve ser do tipo string. {tipoarg.__name__} foi recebido.')
            print(mensagem)    
            return funcao(*args, **kwargs)
        return inner
    return restringe_param_string

@fabrica_decorator('Sucesso')
def invertestring(texto):
    return texto[::-1]

print(invertestring('Texto a inverter'))
#print(invertestring(123))