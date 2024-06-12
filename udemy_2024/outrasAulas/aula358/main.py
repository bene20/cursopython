from pai import Pai
from filho import Filho

p = Pai('Pedro', None)
f = Filho('Lucas', p)
p2 = Pai('Caio', p)
f2 = Filho('Davi', None)

p.show_me()
f.show_me()
p2.show_me()
f2.show_me()