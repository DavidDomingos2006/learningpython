import re
import random

cpf = '097.373.370-50'
cpf_sem_pontos = cpf.replace('.', '').replace('-', '')

#USANDO EXPRESSÕES REGULARES NO LUGAR DE REPLACE
""" cpf_sem_pontos = re.sub(

    r'[^0-9]',
    "",
    cpf
)
 """
#criando 9 numeros aleatórios para gerar CPF
""" num = ''
for digito in range(9):
    num+= str(random.randint(0,9))
print(num)
 """
nove_numeros_iniciais_cpf = cpf_sem_pontos[0:9]

numero_regressivo = 10
soma = 0
for cada_numero in nove_numeros_iniciais_cpf:

    
    soma += int(cada_numero) * numero_regressivo
    #print(f' {cada_numero} * {numero_regressivo} = {soma}')
    numero_regressivo -= 1
soma_multiplicado = soma * 10
resto_de_soma_multiplicacao = soma_multiplicado % 11
primeiro_digito = 0 if resto_de_soma_multiplicacao >=9 else resto_de_soma_multiplicacao
#print(f'O primeiro digito é: {resto_de_soma_multiplicacao}')

##CALCULANDO O SEGUNDO DIGITO DO CPF

#pegando os nove numeros iniciais (string) + o primeiro digito (int). Em uma string

nove_numeros_mais_prim_digito = nove_numeros_iniciais_cpf + str(primeiro_digito)
regressivo_2 = 11
nova_soma = 0
for cada_numero in nove_numeros_mais_prim_digito:

    nova_soma += int(cada_numero) * regressivo_2
    regressivo_2-=1
segundo_digito = (nova_soma* 10) % 11 
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

#VERIFICAÇÃO DO CPF INICIAL COM O VALOR JA VERIFICADO (OU VALOR ENVIADO PELO CLIENTE)

cpf_verificado = f'{nove_numeros_iniciais_cpf}{primeiro_digito}{segundo_digito}'

if cpf_verificado == cpf_sem_pontos: 
    print('CPF valido')
else:
    print('CPF invalido')