import random
import string

def gerar_senha(quantida_de_letras):
    letras = list(string.printable)
    senha = []
    
    for i in range(quantida_de_letras):
        letra = random.choice(letras)
        while letra == [" ", "(","_", ",","","/","´", "`"] :
            
            letra = random.choice(letras)
            
        
        senha.append(letra)
    senha_unida = "".join(senha)
    print(senha_unida)

num_letras = input("Digite o tamanho da senha desejada: ")

gerar_senha(int(num_letras))
