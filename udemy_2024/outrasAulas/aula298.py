import string

template = """
Prezado ${nome},
No dia ${data} foram realizadas ${qtd_tentativas} tentaivas de contato com o telefone ${telefone}.

Favor entrar em contato conosco o quanto antes.
${empresa}
"""
dados = dict(nome='Ana',
             data='20/05/2023',
             telefone='(21)234-5678',
             empresa='José das Couves',
             qtd_tentativas=5)

texto = string.Template(template).substitute(dados)
print(texto)
