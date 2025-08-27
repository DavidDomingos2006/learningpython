'''
num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')

if num1>num2:
    print(f'O primeiro numero digitado - {num1}, é maior que o segundo numero - {num2}')
else:
    print(f'O Segundo numero digitado - {num2}, é maior que o primeiro numero - {num1}')

print(50 * '-')
print('EXERCICIO 2 - Par ou impar?\n')

num1 = input('Digite um numero para saber se ele é par ou impar: ')
if int(num1)%2 != 0:
    print(f"{num1} é impar") 
else:
     print(f"{num1 } é par") 

print(50 * '-')
print('EXERCICIO 3 - imprima um numero enquanto ele for menor que 10?\n')

num1 = 0
num2 = 10
while num1 <=num2:
    print(num1, end='-')
    num1 = num1 +1
    if num1 == (num2 -1):
        print(num1)
        break
'''
'''
print(50 * '-')
print('EXERCICIO 4 - Estrutura de repetição que imprima letra por letra?\n')

nome = 'Nikola tesla'
tamanho = len(nome)

i = 0

while tamanho > i:
    print(nome[i], end='-')
    i = i+1
'''
'''
for i in 'Nikola Tesla':
    
    print(i, end='-')
'''    
# Iteração com for em python é muito diferente de java, a estrutura é enxuta,
# de forma que o sistema ja entende o que o 'i' deve fazer. 
#Outra coisa interessando é que a variavel 'i' não é um inteiro, mas uma string
'''
lista = ['Feijão', 'Massa', 'Cuzcuz', 'Bola', 'Arroz', 'Macarrão', 'Escova', 'Café']

for i in lista:
    print(i)
'''
'''
valor_inicial = int(input("Digite o valor inicial: "))
valor_final = int(input("Digite um valor final: "))
'''
'''
while valor_final>=valor_inicial:
    print(valor_inicial)
    valor_inicial = valor_inicial+1
'''
'''
#OU DA FORMA MAIS FACIL

for i in range(valor_inicial, valor_final + 1):
    print(i)
'''
""" for i in range(0 , 20 +1 ):
    if i % 2 == 0:
        print(i)
 """
""" 
print('Progressão aritimética, defina o primeiro termo e o segundo termo')
termo = int(input("Digite o primeiro termo: \n"))
razao = int(input("Digite a razão: \n"))
print('')

pa = termo + (5 - 1 ) * razao

print(f'Valor da Progressão Aritimética é: {pa}', '\n')

for i in range(termo, pa + razao, razao): #Não entendi bem esse aqui
    print(i)
"""

""" 
print('Imprima a tabuada do numero que eu escolher')

numero_escolhido = int(input("\nDigite o numero: \n"))

for i in range(10+1):
    print(f" {numero_escolhido} x {i} = {numero_escolhido*i}")
"""  


""" 
from time import sleep


print("contagem regressiva\n")

for i in range(10, -1, -1):
    if(i<6):
        print(i)
        sleep(0.2)
    else:
        print(i)
        sleep(1)
print('')   
print("Triiiiiiimmmmmm Acorda\n\n")
"""
""" 
print("Numeros impares de 1 até 100 e sua soma\n")
contador = 0
soma = 0
for i in range(1,100,1):
    if i%2 != 0:
        print(i)
        contador = contador+1
        soma = soma + i
print('')
print(f'foram encontrados {contador} numeros impares\nE a soma deles é {soma}')
"""
""" 
print('Calculo de numeros primos\n')

nume = int(input("Digite um numero para saber se ele é primo: "))
contador = 0

for i in range( 1 , nume +1, +1):
    if nume%i == 0 :
        contador = contador + 1
if contador > 2:
    print(f'{nume} não é primo\nEsse numero é divisivel por {contador} numeros')
elif contador == 2:
    print(f'\n{nume} é um numero primo\n')
"""
""" 
print("Adicionando nomes em uma lista")

nomes=['Wellyda', 'David', 'Rebeka', 'Sônia']
print(f'Lista de nomes antes de acrescentar: {nomes}')
nomes.append('Geraldo')
print(f'Lista de nomes com acrescimo{nomes}')

nomes.insert(3, 'Rayane') #Assim eu acrescento na posição que eu desejar
print(nomes)

nomes.remove('Geraldo')
print(nomes)

print("lista com nomes escolhidos")
print(nomes[1:4])
"""
""" 
print('Criando um dicionário\n')

lista_Compras = dict(Pão = 'R$ 2,59',
                     Açucar = 'R$ 5,29',
                     Café = 'R$ 7,88')
print(lista_Compras)

print('Pesquisando item na lista')

nome_pesquisado = input('Digite um item para verificar se tem na lista:')

for i in (lista_Compras):
    if i == nome_pesquisado:
        print(f'o item {nome_pesquisado} está na lista')
        break
    else:
         print(f'o item {nome_pesquisado} não está na lista')
         break
 """

print('Dicionários podem ser criados a partir de duas listas distintas')

itens_de_compra = ['Arroz', 'Feijão', 'Nutela', 'Agua']
valores_dos_itens = ['2,39', '3,59', '9,85', '2,00']

#agora posso criar o dicionário e ao invés de digitar os dados dentro dela 
#eu puxo os dados de listas um contendo as chaves e outra os valores

lista_compra_completa = dict(Itens = itens_de_compra, Preços = valores_dos_itens)

print(lista_compra_completa)
print(type(lista_compra_completa))

