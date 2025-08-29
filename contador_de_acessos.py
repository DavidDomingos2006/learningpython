def criar_contador():

    contador = 0

    def somar_contador():
        
        nonlocal contador 
        
        contador +=1

        return contador

    return somar_contador

acesso_inicial = criar_contador()
segundo_acesso = criar_contador()

print(acesso_inicial())
print(acesso_inicial())
print(acesso_inicial())
print(acesso_inicial())
print(segundo_acesso())

    