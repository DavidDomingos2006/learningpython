# Strings

# Aspas Simples
print('David Domingos')

# Aspas Duplas
print("David Domingos")

# Escape - Pula o proximo caractere na leitura normal
print("David \"Domingos") #Perceba que agora ao imprimir ele aparecerá "Domingos com aspas no começo
# O que é que o sistema fez, ele pula a função principal das aspas com separador de strings e utiliza ela como aspas normais.
#Caso eu queira que as aspas apareçam eu preciso repeti-las
print("David \"Domingos\"")
print("David \3Domingos\3") #nada acontece a não ser a impressão do nome normal

# r - Essa função faz exibir o caracter especial \ que não aparece normalmente.
print(r"David \"Domingos\"")

#PARA UMA FORMA MAIS FACIL DE USAR ASPAS É SOMENTE USAR ASPAS SIMPLES E ASPAS DUPLAS
print('David "Domingos"')


