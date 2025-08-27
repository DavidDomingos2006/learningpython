
nome = input("Digite seu nome: ").strip() #função strip tira os espaços digitados antes e depois 
idade = input('Digite sua idade: ').strip()


if (nome or idade) == "" or (nome or idade) == " ":
    print('Desculpe você deixou campos vazios')
else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é: {nome[-1::-1]}')
      
           
if nome.count(" ") > 0: #função count('x') conta quantos 'x' tem na string
     print(f'Seu nome contém {nome.count(" ")} espaços')
else:
    print('Seu nome não contém espaços')

print(f'Seu nome contem {len(nome.replace(" ", ""))} letras') #função replace serve para substituir (1,2) o primeiro agumento pelo segundo argumento, se o primeiro existir na palavra
print(f'A primeira letra do seu nome é: {nome[0]}')
print(f'A ultima letra do seu nome é: {nome[-1]}')

""" 
def boas_vindas():
    print("Bem vindo ao mundo python!")

def calcular_area_retangulo(largura, altura):
    print(f'A área do triangulo é: {largura*altura}')

def eh_par(num):
    return num%2 == 0

boas_vindas()

print(50 * '-')

print("Insira dois numeros para calcular a area do triangulo")

calcular_area_retangulo(int(input('Digite a largura: ')), int(input('Digite a altura: ')))
print(50 * '-')
if eh_par(int(input("Digite um numero para saber se é impar ou par: "))):
    print('Par')
else:
    print("Impar")

print(50 * "-")
 """
""" 
def calcular_media(num):
    if not num:
                return 0.0
    soma = sum(num)
    media = soma/len(num)
    return media 

notas_alunos = [9,8,9,5]
media_final = calcular_media(notas_alunos)
print(f'As notas do aluno foram: {notas_alunos}')
print(f"A média do aluno foi: {media_final}")
 """
""" 
try:
   while True:
        idade_str = input("Digite sua idade: ").strip()
        if not idade_str:
            print("Dado não poder ser vazio")
            continue
except:
    print("Algo errado")
 """