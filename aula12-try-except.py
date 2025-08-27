#diferente de Java onde tinha o try catch, aqui em python temos o try except, funciona da mesma
#forma, o codigo tenta um bloco caso não seja possivel ele cai para uma exceção

try:
    num = int(input("Digite um numero e vou dobra-lo: "))
    dobrado = print(f'Dobrei: {num*2}')
    
except:
    print("Não foi possivel pois você não digitou um numero invalido!")