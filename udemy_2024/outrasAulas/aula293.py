import csv

# with open('aula293.csv', 'r') as arqcsv:
#     leitor = csv.reader(arqcsv)

#     for linha in leitor:
#         print(linha[0], linha[1], linha[2])

# with open('aula293.csv', 'r') as arqcsv:
#     leitor = csv.DictReader(arqcsv)

#     for linha in leitor:
#         print(linha)

# csv_string = [
#     ['Nome','Idade','Endereço'],
#     ['Ana','12','Rua Z, 23, "Centro"'],
#     ['Beto','27','Rua A, 35, "Sul"'],
#     ['Caio','32','Ruz X, 321, "Norte"']
# ]

# with open('aula293_b.csv', 'w') as arqcsv:
#     escritor = csv.writer(arqcsv)

#     for item in csv_string:
#         escritor.writerow(item)

csv_dict = [
    {'Nome': 'Ana', 'Idade': '12', 'Endereço': 'Rua Z, 23, "Centro"'},
    {'Nome': 'Beto', 'Idade': '27', 'Endereço': 'Rua A, 35, "Sul"'},
    {'Nome': 'Caio', 'Idade': '32', 'Endereço': 'Ruz X, 321, "Norte"'}
]

with open('aula293_c.csv', 'w') as arqcsv:
    escritor = csv.DictWriter(arqcsv, fieldnames=csv_dict[0].keys())
    escritor.writeheader()
    for item in csv_dict:
        escritor.writerow(item)        