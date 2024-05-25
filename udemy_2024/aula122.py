p1=dict(nome='Ana', idade=25, numeros=[1,2,3])
p2=p1.copy()
p1['numeros'][1]=90
print(p1)
print(p2)