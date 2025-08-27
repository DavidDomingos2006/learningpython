#2ª formatação é usando a função format depois da string

# nome = 'David'
# sobrenome = 'Domingos'
# ultimo_nome = 'da Silva'
# idade = 40

# nome_completo = "".format(nome, sobrenome, ultimo_nome, idade)
# # dentro de nome_completo eu uso argumentos que serão usados para a string
# # como em um vetor, o que será impresso está no começo dentro das aspas,
# #  o que está em .format serve como parâmetro ou melhor argumento para 
# # o que será impresso junto com o que está dentro das aspas. esse primeiro não
# #imprime nada, mas veja o proximo.
# nome_completo = "Meu nome é: {} {} {}".format(nome, sobrenome, ultimo_nome)
# #por usarmos essa função ao abrir as chaves ele automáticamente puxa pela ordem,
# #mas eu posso definir essa ordem também veja abaixo:
# nome_completo = "Meu nome é: {1} {0} {2}".format(nome, sobrenome, ultimo_nome)

# print(nome_completo, "\n\n")
# #Eu ainda poderia criar uma variável prévia contendo essas chaves ja na ordem para
# #receber esses dados por exemplo 
# nome2 = "Wellyda"
# Sobrenome2 = "Cristina"
# Ultimo_nome2 = "da Silva"

# impressao = 'Meu nome é {} {} {}'
# #está variável impressão ja está prevendo que será usada em outra string que será
# #formatada para impressão
# formatada = impressao.format(nome2,Sobrenome2, Ultimo_nome2)
# #na variavel impressão eu defini que ela receberia argumentos e na variável
# #formatada eu faço ela receber a string impressão e uso a função format que é uma 
# #função de string.
# print(formatada)

# #por fim as chaves vazias possuem valores padrões que iniciam de 0 em diante
# #mais uma coisa eu posso editar dentro da chave uma formatação float e posso tbm 
# #criar parâmetros, vamos usar a variavel idade, nome e criaremos altura

# altura = 1.70 #lembre que flot so imprime uma casa decimal, vamos consertar isso.
# idade_nome = "Nome: {1}\nIdade: {0}\nAltura {2:.2f}".format(idade, nome, altura)
# #aqui fiz questão de inverter a posição de nome e idade para usarmos os numeros
# #dos vetores.
# #OBSERVE QUE NAS CHAVES DE 'ALTURA' USAMOS A FORMATAÇÃO DE NUMEROS DECIMAIS.
# print(idade_nome)
# #Caso a chave esteja vazia{} usamos apenaso comando {:.2f}
# #Agora vamos aprender os PARÂMETROS

# nome = 'Luiz'
# idade3 = 23
# forma = "{nomeCliente} tem {idadeCliente} anos" #esses nomes dentro da chave serão
# #os parâmetros que usaremos
# print(forma.format(nomeCliente=nome, idadeCliente=idade3))

#outras formatações para f string

variavel = 'ABC'

print(f'{variavel: >10}') #esta formatação permite preencher com o algarismo escolhido
#a quantidade de espaços vazios a esquerda
print(f'{variavel: <10}') #direita
print(f'{variavel: ^10}') #centro

mensagem = 'Este é um otimo dia'

#podemos fatiar essa string e pesquisar pedaços dela

print(mensagem[3:]) #entre colchetes pode ficar da seguinte forma [inicial: final: passo]
#neste caso comecei do indice 3
#Este é um otimo dia
#0123456789... por isso a impressão começa da letra 'e' e vai até o final pois com não 
#decidi o final, ele fica definido automaticamente com o ultimo indice

print(mensagem[:10])#definindo apenas o final e o inicio é automáticamente configurado
print(mensagem[::2])#agora definindo apenas o passo que a letras serão exibidas, neste caso a cada duas letras

impares = '123456789'

print(impares[0::2])

#os indices também podem ser representados por numeros negativos
# Este é um otimo dia
#       ...-987654321
print(mensagem[-1:-13:-1])#se eu não definir o passo como -1 ou -2 ou 
#algum numero negativo de passo, a impressão será " "

print("Vamos fazer uso da função len(), ela me retorna o tamanho da string")

print(mensagem[4:len(mensagem)])


