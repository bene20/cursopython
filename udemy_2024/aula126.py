import os
lista=['Ana', 'Beto', 'Caio']
s1=set(lista)
s2=set('Ebenezer')
s3=set({1,2,3,(4,5,6)})
print(s1)
print(lista)
print(s3)

conj=set((2,))#  ((30,40,2,3,4))
print(conj)

print(type(2))
print(type((2)))
print(type((2,)))

s4=set()
s4.add('Lista')
print(s4)

os.system('clear')
s5=set({1,2,3})
s5.update({'Teste',4,5,6})
#s5.update(('Teste',))
print(s5)