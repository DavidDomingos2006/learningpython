#print("1"+ 1)
# não da para realizar esse processo, se quisessemos que fosse
# impresso 11 teriamos que tira o + e colocar uma virgula dividindo os argumentos
print("1",1, sep="")
# MAS se a intenção é realizar uma soma então precisamos converter um dos tipos.

print(int("1") + 1 ) #podemos usar isso para todos os tipos primitivos 
# int, str, float e bool...
