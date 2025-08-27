
while True:
    try:
        num = int(input('Digite um numero: '))
        if num%2 == 0: 
            print('Seus numero é par') 
            break
        else: 
            print('Numero impar')
            break
    except:
        print('Não é um numero inteiro')

""" 
try:
    hora = int(input('Que horas são: '))
    if hora >= 0 and hora <=11:
        print('Bom dia')
    elif hora >=12 and hora <= 17:
        print("Boa tarde")
    elif hora >=18 and hora <=23:
        print('Boa noite') 
except:
    print("Voce não digitou uma valor correto 'ex: 1...2...14' "\
          'digite apenas o valor da hora 1 ou 14' \
          '')
   """  
""" 
try:
    nome = input("Digite o seu primeiro nome: ")
    tamanho = len(nome)
    
    if tamanho <=4:
        print('Seu nome é curto')
    elif tamanho >4 and tamanho <=6:
        print('Seu nome é normal')
    else:
        print("Seu nome é muito grande")

except:
    print("Voce digitou um valor invalido")
 """
