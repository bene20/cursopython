import random

for i in range(1,5):
    print(random.randrange(1, 20, 3))

for i in range(1,5):
    print(random.uniform(0, 20))    

nomes = ['Ana', 'Beto', 'Caio', 'Davi']
random.shuffle(nomes)
print(nomes)

nomes = ['Ana', 'Beto', 'Caio', 'Davi']
print(random.sample(nomes, k=2))
print(random.choices(nomes, k=3))
print(random.choice(nomes))
print("="*10)
random.seed(0)
print(random.choice(nomes))

import time
meu_seed = time.time()
print(f'Usando o seed {meu_seed}')
for i in range(1,5):
    random.seed(meu_seed)
    print(random.randint(1,100))