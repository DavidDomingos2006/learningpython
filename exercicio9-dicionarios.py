frase = 'o rato roeu a roupa do rei de roma no dia treze'

dicionario = {} #criado usando chaves

for i in frase.split():
    if i in dicionario:
        dicionario[i] += 1
    else:
        dicionario[i] = 1

print(dicionario)
print(f'\n')
#posso fazer uma lista de dicionários

estoque = [] #chaves para criar lista
estoque = [{'produto': 'arroz', 'preço': 3.50, 'quantidade': 15}, 
           {'produto': 'feijão', 'quantidade': 7, 'preço': 5.90},
           {'produto': 'Macarrão', 'preço': 4.90, 'quantidade': 12}
           ]
total = 0 #se eu não definir o 'que é' total dará um erro, pois o sistema não sabe 
          #o que está fazendo! Se é uma concatenção, uma soma, 
          #um acrescimo em uma lista...
for qtdade in estoque:
    total += qtdade['quantidade']
print(total)
print(f'\n')
#exercicio pratico criando dicinario sobre dados de carro

sandero = {'Marca': 'Renault', 'Modelo': '1.0 stepway', 'Ano': 2011}
#adicionando cor apos criação do dicionário
sandero['cor'] = 'Preto'
print(f'{sandero} \n')

tradutor_de_fruta = {'MAÇA': 'APPLE', 'LARANJA': 'ORANGE'}

fruta = input('Digite uma fruta para saber sua tradução em ingles')

while fruta in tradutor_de_fruta:
    print(f'a tradu é {tradutor_de_fruta[fruta]}')
    fruta = input('Digite uma fruta para saber sua tradução em ingles')