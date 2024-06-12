import json

pessoa={
    'nome': 'Ana',
    'idade': 25,
    'pets': [
        {'tipo': 'canino', 'nome': 'Pepperoni', 'idade': 7},
        {'tipo': 'canino', 'nome': 'Minuim', 'idade': 8},
        {'tipo': 'felino', 'nome': 'Mingau', 'idade': 3},
    ],
    'endereco' : {
        'logradouro': 'Rua sete',
        'numero': 125,
        'bairro': 'Grajaú',
        'lotes': [3,4,5,12]
    }
}

with open('meusdados.json', 'w', encoding='utf-8') as arquivo:
    json.dump(pessoa, arquivo, indent=2, ensure_ascii=True)

with open('meusdados.json', 'r', encoding='utf-8') as arquivo:
    pessoa2=json.load(arquivo)    
    print(pessoa2)