nome = "David Domingos"
altura = 1.70
peso = 78.30
imc = peso/ altura**2
print("Nome: ", nome, "\nAltura: ", altura, "\nPeso: "
      ,peso)
print("IMC =",imc)

#OUTRA FORMA para não haver tanta virgula no print

impressao = f"Nome: {nome},\nAltura: {altura:.2f}, \nPeso: {peso:.2f}\nO seu IMC é: {imc:.2f}"
#Criamos uma string usando um f na frente dela, isso nos permite criar uma
#string formatável, os nomes que estão entre chaves são justamente as variáveis
#Veja que neste formato eu pude alterar a forma de como a variável altura vai ser
#impressa, com duas casas decimais.
print(impressao)

