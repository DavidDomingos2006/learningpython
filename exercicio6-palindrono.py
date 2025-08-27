#CRIANDO PALINDRONOS

nome = list(input("Digite um nome para verificar se tem o palidrono dele: "))
palindrono_novo = []

for i in range(len(nome)-1, -1, -1):
    #palindrono_novo.insert(i, nome[i])
    palindrono_novo.append(nome[i])
    print(palindrono_novo)

if palindrono_novo == nome:
    print("Este nome é um palidrono")
else:
    print("Não é um palidrono")


