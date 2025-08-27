import random


palavras = ['Arroz', 'Buzina', 'Super']

palavra_aleatoria = list(random.choice(palavras).upper())
palavra_temp = ["_" for _ in palavra_aleatoria] #isso cria uma lista com as letras da palavra aleatoria ['S', 'U','P','E','R']
#Essa forma é a melhor pois eu posso futuramente substituir cada indice por um novo valor
#neste caso eu criei a palavra com '_' underlines para boa visibilidade.

while True:
    tentativa = input("Digite uma letra para saber se existe na palavra: ").upper()
    indice = 0
    
    for i in palavra_aleatoria:
        if tentativa == palavra_aleatoria[indice]:
            palavra_temp[indice] = tentativa
        
            indice+=1
            
        else:
            
            indice+=1

    
    print(palavra_temp)
    palavra_certa = "".join(palavra_temp) #apos cada rodada essa função vai juntando as letras da lista em uma nova string.
    if palavra_temp == palavra_aleatoria:
        print(f"A palavra é: {palavra_certa}")
        break   
  