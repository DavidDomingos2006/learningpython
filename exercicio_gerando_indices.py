#codigo 1
""" 
lista = ['Maria', 'Helena', 'Luiz']
indice = 0
lista.append('João')
for nome in lista:
    print(f'indice {indice}, nome {nome}')
    indice +=1 
 """
#codigo 2 mais confiavel
""" 
lista = ['maria', 'helena', 'Luiz']
indices = range(len(lista))
for indice in indices:
    print(indice, lista[indice])
 """

#codigo 3 mais eficiente e confiavel
lista = ['maria', 'helena', 'Luiz']

for indice ,nome in enumerate(lista):
     print(f'{indice} {nome} ')