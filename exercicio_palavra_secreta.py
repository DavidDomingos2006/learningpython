
palavra_secreta = 'CASA'
letras_certas=''
palavra_correta=''
chances=3

while len(letras_certas)!=len(palavra_secreta):
    
    letra_tentada = input('Digite sua letra: ').upper()

    if letra_tentada in letras_certas:
        chances-=1
        print(f'Voce ja digitou essa letra, agora só tem {chances} chances' if chances>0 else 'Acabaram suas chances.')

    if letra_tentada in palavra_secreta:
        letras_certas += letra_tentada
         
                
    else:
        chances-=1
        print(f'Só tem {chances} chances' if chances >0 else 'Suas chances acabaram')

for letras in palavra_secreta:
    if letras in letras_certas:
        palavra_correta+= letras

print(palavra_correta)